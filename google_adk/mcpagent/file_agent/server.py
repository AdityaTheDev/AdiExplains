import os
from mcp.server.fastmcp import FastMCP

BASE_DIR = os.path.join(os.path.dirname(__file__), "files")

# Create files directory if it doesn't exist
os.makedirs(BASE_DIR, exist_ok=True)

mcp = FastMCP("file-mcp-server")


@mcp.tool()
def list_files() -> list[str]:
    """List all files in the files directory"""
    return [
        f for f in os.listdir(BASE_DIR)
        if os.path.isfile(os.path.join(BASE_DIR, f))
    ]


@mcp.tool()
def read_file(filename: str) -> str:
    """Read the contents of a file"""
    file_path = os.path.join(BASE_DIR, filename)

    if not os.path.exists(file_path):
        return "File not found"

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


@mcp.tool()
def write_file(filename: str, content: str) -> str:
    """Write content to a file"""
    file_path = os.path.join(BASE_DIR, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return "OK"


if __name__ == "__main__":
    mcp.run(transport="stdio")
