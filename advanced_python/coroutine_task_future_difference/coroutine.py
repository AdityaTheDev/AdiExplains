import asyncio

async def fetch_data():
    print("Fetching data")
    await asyncio.sleep(2)
    print("Data received")

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())