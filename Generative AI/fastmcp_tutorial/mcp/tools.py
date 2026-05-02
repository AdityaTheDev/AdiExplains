from fastmcp.tools import tool
from fastmcp.resources import resource
from fastmcp.prompts import prompt



@tool(name="multiply")
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b

@tool(name="add")
def add(a: float, b: float) -> float:
    """Adds two numbers together."""
    return a + b

@resource("data://config")
def get_config() -> dict:
    return {"theme": "dark", "version": "1.0"}

@prompt(name="analyze_data")
def analyze_data(data_points: list[float]) -> str:
    formatted_data = ", ".join(str(point) for point in data_points)
    return f"Please analyze these data points: {formatted_data}"