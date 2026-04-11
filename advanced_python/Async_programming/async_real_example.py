import asyncio
import aiohttp
import time

URL = "https://randomuser.me/api/"

async def fetch_user(session):
    async with session.get(URL) as response:
        data = await response.json()
        name = data["results"][0]["name"]["first"]
        return name

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_user(session) for _ in range(14)]
        results = await asyncio.gather(*tasks)

        for name in results:
            print(name)

start = time.time()

asyncio.run(main())

end = time.time()

print(f"\nTotal time (async): {end - start:.2f} seconds")