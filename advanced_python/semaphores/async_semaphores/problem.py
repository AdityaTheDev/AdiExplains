# PROBLEM: gather() starts ALL tasks at the same time
import asyncio
import time

running = 0   # how many tasks are running right now
max_concurrent_calls = 0      # the highest number we saw at one moment


async def fetch(i):
    global running, max_concurrent_calls
    running += 1
    max_concurrent_calls = max(max_concurrent_calls, running)
    print(f"Task {i} started   (running now: {running})")
    await asyncio.sleep(2)            #pretend this is a web request
    print(f"Task {i} done")
    running -= 1


async def main():
    start = time.time()
    await asyncio.gather(*(fetch(i) for i in range(1, 9)))   # 8 tasks
    print(f"\nMax concurrent calls at same time: {max_concurrent_calls}")
    print(f"Total: {time.time() - start:.1f} s")


asyncio.run(main())