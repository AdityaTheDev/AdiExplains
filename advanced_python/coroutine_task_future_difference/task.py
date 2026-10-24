import asyncio
from time import perf_counter

async def fetch_data(name, delay):
    print(f"Started {name}")
    await asyncio.sleep(delay)
    print(f"Finished {name}")
    return name

async def main():
    start_time = perf_counter()
    task1 = asyncio.create_task(fetch_data("API 1", 2))
    task2 = asyncio.create_task(fetch_data("API 2", 2))

    print("Tasks scheduled")

    result1 = await task1
    result2 = await task2
    end_time = perf_counter()

    print(f"RESULT : {result1}, {result2}")
    print(f"Total time taken: {end_time - start_time} seconds")

asyncio.run(main())