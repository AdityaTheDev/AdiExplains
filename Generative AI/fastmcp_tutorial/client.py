import asyncio
from fastmcp import Client
from server import mcp



client = Client(mcp)



async def main():
    async with client:
        # Basic server interaction
        await client.ping()

        # List available operations
        tools = await client.list_tools()
        resources = await client.list_resources()
        prompts = await client.list_prompts()

        print("Available Tools:", tools)
        print("Available Resources:", resources)
        print("Available Prompts:", prompts)

        # Execute operations
        # result = await client.call_tool("add", {"a": 5, "b": 3})
        # print("Result of add(5, 3):", result.content[0].text)

        # result = await client.call_tool("multiply", {"a": 5, "b": 3})
        # print("Result of multiply(5, 3):", result.content[0].text)

asyncio.run(main())