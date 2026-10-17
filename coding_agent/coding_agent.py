import inspect
import json
import os
import re

from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from google import genai
from google.genai import types

# set GOOGLE_API_KEY in a .env file in the same directory.
load_dotenv()


class CodingAgent:
    """A text-based coding agent that calls Python tools using an LLM."""

    TOOL_CALL_PATTERN = re.compile(
        r"^tool:\s*([A-Za-z_]\w*)\((.*)\)\s*$"
    )

    SYSTEM_PROMPT_TEMPLATE = """
You are a coding assistant that solves programming tasks using  tools available.

Available tools:
{available_tools_description}

TOOL-CALL PROTOCOL:
1. When you need a tool, output exactly one line in this format:
   tool: TOOL_NAME({{"argument": "value"}})

2. Output nothing else alongside a tool call.
3. Tool arguments must be valid JSON using double quotes.
4. Use only registered tool names and their declared arguments.
5. After receiving tool_result(...), inspect the result before proceeding.
6. When the task is complete, respond normally without calling a tool.
7. Do not repeat a successful tool call unnecessarily.
8. Never claim an operation succeeded unless the result confirms success.
9. If a tool fails, inspect the error before retrying.
10. Ask for clarification if the request is ambiguous.

All file operations must remain inside the configured workspace.
"""

    def __init__(
        self,
        model_name: str = "gemini-2.5-flash",
        workspace_path: str | Path | None = None,
        max_tool_calls_per_turn: int = 10,
        max_reasoning_steps: int = 15,
    ):
        # Model configuration
        self.model_name = model_name
        self.max_tool_calls_per_turn = max_tool_calls_per_turn
        self.max_reasoning_steps = max_reasoning_steps

        # Workspace configuration
        configured_workspace = (
            workspace_path
            or os.getenv("AGENT_WORKSPACE")
            or Path.cwd() / "agent_workspace"
        )

        self.workspace_path = Path(configured_workspace).resolve()
        self.workspace_path.mkdir(parents=True, exist_ok=True)

        # Initialize the Google GenAI client
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError(
                "GOOGLE_API_KEY was not found. "
                "Set it in your .env file."
            )

        self.genai_client = genai.Client(api_key=api_key)

        # Register the Python functions available to the agent
        self.available_tools :dict[str, callable] = {
            "read_file": self.read_file,
            "list_files": self.list_files,
            "create_file": self.create_file,
            "edit_file": self.edit_file,
        }

        # Build instructions describing the available tools
        self.agent_system_prompt = self._build_system_prompt()

        # Store conversation messages across user turns
        self.conversation_history: list[dict[str, str]] = []

    # tool implementations
    def _resolve_workspace_path(self, file_path: str) -> Path:
        """Resolve a path and prevent access outside the workspace."""

        requested_path = Path(file_path)

        if not requested_path.is_absolute():
            requested_path = self.workspace_path / requested_path
            #hello.py
           # D:Python Projects/adiexplains_git/AdiExplains/agent_workspace/hello.py

        resolved_path = requested_path.resolve()

        if not resolved_path.is_relative_to(self.workspace_path):
            raise ValueError(
                "Access denied: path must remain inside the workspace."
            )

        return resolved_path

    def read_file(self, file_path: str) -> str:
        """Read and return the contents of a file."""

        resolved_path = self._resolve_workspace_path(file_path)

        if not resolved_path.is_file():
            raise FileNotFoundError(
                f"File does not exist: {file_path}"
            )

        return resolved_path.read_text(encoding="utf-8")

    def list_files(self, directory_path: str = ".") -> str:
        """List the files and directories at a workspace location."""

        resolved_path = self._resolve_workspace_path(directory_path)

        if not resolved_path.is_dir():
            raise NotADirectoryError(
                f"Not a directory: {directory_path}"
            )

        directory_entries = sorted(
            entry.name + ("/" if entry.is_dir() else "")
            for entry in resolved_path.iterdir()
        )

        return json.dumps(directory_entries, ensure_ascii=False)

    def create_file(
        self,
        file_path: str,
        content: str,
        overwrite: bool = False,
    ) -> str:
        """Create a file, optionally overwriting an existing file."""

        resolved_path = self._resolve_workspace_path(file_path)

        if resolved_path.exists() and not overwrite:
            raise FileExistsError(
                f"File already exists: {file_path}. "
                "Set overwrite=true to replace it."
            )

        resolved_path.parent.mkdir(parents=True, exist_ok=True)
        resolved_path.write_text(content, encoding="utf-8")

        return f"Successfully created or updated: {file_path}"

    def edit_file(
        self,
        file_path: str,
        text_to_replace: str,
        replacement_text: str,
    ) -> str:
        """Replace the first occurrence of text inside a file."""

        resolved_path = self._resolve_workspace_path(file_path)

        if not resolved_path.is_file():
            raise FileNotFoundError(
                f"File does not exist: {file_path}"
            )

        original_content = resolved_path.read_text(encoding="utf-8")

        # Allow an empty file to be populated.
        if original_content == "" and text_to_replace == "":
            updated_content = replacement_text

        elif text_to_replace == "":
            raise ValueError(
                "Cannot replace an empty string in a non-empty file."
            )

        elif text_to_replace not in original_content:
            raise ValueError(
                f"Text to replace was not found in {file_path}."
            )

        else:
            updated_content = original_content.replace(
                text_to_replace,
                replacement_text,
                1,
            )

        resolved_path.write_text(
            updated_content,
            encoding="utf-8",
        )

        return f"Successfully edited: {file_path}"

    # tool registration and system prompt construction

    def _build_system_prompt(self) -> str:
        """Describe registered tools and their arguments to the LLM."""

        tool_descriptions = []

        for tool_name, tool_function in self.available_tools.items():
            function_signature = inspect.signature(tool_function)
            function_description = (
                inspect.getdoc(tool_function)
                or "No description provided."
            )

            tool_descriptions.append(
                f"- {tool_name}{function_signature}\n"
                f"  Description: {function_description}"
            )

        available_tools_description = "\n".join(tool_descriptions)

        return self.SYSTEM_PROMPT_TEMPLATE.format(
            available_tools_description=available_tools_description
        )

    # Tool call parsing and execution

    def parse_tool_call(
        self,
        assistant_response: str,
    ) -> tuple[str, dict[str, Any]] | None:
        """
        Parse a response such as:
        tool: read_file({"file_path": "main.py"})

        Return (tool_name, tool_arguments), or None if the response
        does not match the tool-call protocol.
        """

        tool_call_match = self.TOOL_CALL_PATTERN.fullmatch(
            assistant_response.strip()
        )

        if tool_call_match is None:
            return None

        tool_name = tool_call_match.group(1)
        arguments_json = tool_call_match.group(2)

        try:
            tool_arguments = json.loads(arguments_json)
        except json.JSONDecodeError:
            return None

        if not isinstance(tool_arguments, dict):
            return None

        return tool_name, tool_arguments

    def execute_tool_call(
        self,
        tool_name: str,
        tool_arguments: dict[str, Any],
    ) -> dict[str, Any]:
        """Validate and execute a registered Python tool."""

        tool_function = self.available_tools.get(tool_name)

        if tool_function is None:
            return {
                "success": False,
                "error": f"Unknown tool: {tool_name}",
            }

        try:
            # Validate argument names and required parameters.
            inspect.signature(tool_function).bind(**tool_arguments)

            # Execute the actual Python function.
            tool_output = tool_function(**tool_arguments)

            return {
                "success": True,
                "result": tool_output,
            }

        except Exception as execution_error:
            return {
                "success": False,
                "error": (
                    f"{type(execution_error).__name__}: "
                    f"{execution_error}"
                ),
            }

    # llm interaction

    def _call_model(self) -> str:
        """Send the conversation to Gemini and return its text."""

        model_contents = []

        for conversation_message in self.conversation_history:
            message_role = conversation_message["role"]

            # Gemini uses "model" for assistant messages.
            gemini_role = (
                "model" if message_role == "assistant" else "user"
            )

            model_contents.append(
                types.Content(
                    role=gemini_role,
                    parts=[
                        types.Part.from_text(
                            text=conversation_message["content"]
                        )
                    ],
                )
            )

        model_response = self.genai_client.models.generate_content(
            model=self.model_name,
            contents=model_contents,
            config=types.GenerateContentConfig(
                system_instruction=self.agent_system_prompt,
                temperature=0.2,
            ),
        )

        return model_response.text or ""

    # One user turn
    def run_turn(self, user_message: str) -> str:
        """
        Process one user message.

        The agent may call the model multiple times and execute tools
        before returning its final response.
        """

        self.conversation_history.append({
            "role": "user",
            "content": user_message,
        })

        tool_calls_this_turn = 0
        executed_tool_signatures = set()

        for step_number in range(self.max_reasoning_steps):
            assistant_response = self._call_model()

            parsed_tool_call = self.parse_tool_call(
                assistant_response
            )

            # If the response is not a valid tool call, treat it
            # as the assistant's final answer.
            if parsed_tool_call is None:
                self.conversation_history.append({
                    "role": "assistant",
                    "content": assistant_response,
                })
                return assistant_response

            tool_name, tool_arguments = parsed_tool_call

            # Preserve the assistant's tool request in the history.
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_response, #contains tool call 
            })

            # Build a signature to detect identical calls in this turn.
            tool_call_signature = (
                tool_name,
                json.dumps(tool_arguments, sort_keys=True),
            )
            print(f"===TOOL EXECUTION===\nExecuting tool: {tool_name} with arguments: {tool_arguments}")

            if tool_call_signature in executed_tool_signatures:
                final_response = (
                    f"Stopped because the tool call '{tool_name}' "
                    "was repeated with the same arguments."
                )
                self.conversation_history.append({
                    "role": "assistant",
                    "content": final_response,
                })
                return final_response

            if tool_calls_this_turn >= self.max_tool_calls_per_turn:
                final_response = (
                    "Stopped because the maximum number of tool "
                    "calls for this turn was reached."
                )
                self.conversation_history.append({
                    "role": "assistant",
                    "content": final_response,
                })
                return final_response

            executed_tool_signatures.add(tool_call_signature)
            tool_calls_this_turn += 1

            # Execute the requested Python function.
            tool_result = self.execute_tool_call(
                tool_name,
                tool_arguments,
            )

            # Feed the tool result back to the model as conversation text.
            tool_result_message = (
                f"tool_result({json.dumps(tool_result, ensure_ascii=False)})"
            )

            self.conversation_history.append({
                "role": "user",
                "content": tool_result_message,
            })

        final_response = (
            "Stopped because the maximum number of agent steps was reached."
        )
        self.conversation_history.append({
            "role": "assistant",
            "content": final_response,
        })
        return final_response

    # interactive terminal interface

    def run(self) -> None:
        """Start an interactive conversation in the terminal."""

        print("Coding agent started. Type 'exit' to quit.")
        print(f"Workspace: {self.workspace_path}")

        while True:
            try:
                user_message = input("\nYou: ").strip()

                if user_message.lower() in {"exit", "quit"}:
                    print("Coding agent stopped.")
                    break

                if not user_message:
                    continue

                assistant_response = self.run_turn(user_message)
                print(f"\nAssistant: {assistant_response}")

            except KeyboardInterrupt:
                print("\nCoding agent stopped.")
                break


if __name__ == "__main__":
    coding_agent = CodingAgent()
    coding_agent.run()
