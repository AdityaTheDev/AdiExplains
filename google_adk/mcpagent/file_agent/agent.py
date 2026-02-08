import os
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from mcp import StdioServerParameters
from dotenv import load_dotenv

load_dotenv()

here= os.path.dirname(__file__)
server_path = os.path.join(here, "server.py")

file_mcp = StdioServerParameters(
    command="python",
    args=[server_path],
    env=None,
)


root_agent = Agent(
    name="file_agent",
    model="gemini-2.5-flash",
    description="An agent that can manage files using a file management MCP server.",
    instruction="""
    Help the user manage files.
    You can list, read, and write files using tools.
    """,    
    tools=[MCPToolset(connection_params=file_mcp)],
)
