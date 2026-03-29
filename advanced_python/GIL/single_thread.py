import time

def task():
    count = 0
    for _ in range(5 * 10**7):
        count += 1

start = time.time()

task()
# task()

total_time = time.time() - start

print("Single thread:", total_time)