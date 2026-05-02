from fastmcp import FastMCP
from fastmcp.server.providers import FileSystemProvider
from pathlib import Path

mcp = FastMCP("MyServer", providers=[FileSystemProvider(Path(__file__).parent / "mcp")])

if __name__ == "__main__":
    mcp.run()