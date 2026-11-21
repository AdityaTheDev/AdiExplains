# A race condition WITHOUT a semaphore.
# 4 threads each add 1 to a shared counter, 100 times.
# The correct final answer is 4 x 100 = 400.

import threading
import time

count = 0  # the shared "counter" that every thread reads and writes


def add():
    global count
    for i in range(100):
        temp = count           # step 1: read the current value
        time.sleep(0.001)      # step 2: a tiny delay (another thread can start in here)
        count = temp + 1       # step 3: write back the old value plus 1


threads = []
for i in range(4):
    t = threading.Thread(target=add)
    t.start()
    threads.append(t)

# Wait for all 4 threads to finish before printing the result.
for t in threads:
    t.join()

# The result is far below 400 because threads overwrite each other's updates.
print("Expected 400, got", count)