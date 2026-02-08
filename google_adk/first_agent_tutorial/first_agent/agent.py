from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search


def add(a, b):
    """Returns the sum of a and b"""
    return a + b


def subtract(a, b):
    """Returns the difference of a and b"""
    return a - b


def multiply(a, b):
    """Returns the product of a and b"""
    return a * b


def divide(a, b):
    """Returns the division of a by b"""
    if b == 0:
        return "Error: Division by zero"
    return a / b


def modulus(a, b):
    """Returns the remainder when a is divided by b"""
    if b == 0:
        return "Error: Modulus by zero"
    return a % b


def power(a, b):
    """Returns a raised to the power of b"""
    return a ** b


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Don\'t answer using existing knowledge. Always answer user questions using the available tools.',
    tools=[add, multiply, subtract, divide, modulus, power],
)
