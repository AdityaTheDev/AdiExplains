import asyncio
from time import perf_counter

async def fetch_data(name, delay):
    print(f"Started {name}")
    await asyncio.sleep(delay)
    print(f"Finished {name}")
    return name



async def main():
    start_time = perf_counter()
    results = await asyncio.gather(
        asyncio.create_task(fetch_data("API 1", 2)),
        asyncio.create_task(fetch_data("API 2", 1)),
        asyncio.create_task(fetch_data("API 3", 3)),
    )
    end_time = perf_counter()

    print(results)
    print(f"Total time taken: {end_time - start_time} seconds")

asyncio.run(main())