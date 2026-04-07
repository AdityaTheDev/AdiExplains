import time
import asyncio

async def task(task_id):
    print(f"Task {task_id} started")
    await asyncio.sleep(2)
    print(f"Task {task_id} completed")


async def main():
    await asyncio.gather(task(1), task(2))

start=time.time()
asyncio.run(main())
end=time.time()
print(f"Total time taken: {end-start} seconds")

# asyncio.run(task(1))