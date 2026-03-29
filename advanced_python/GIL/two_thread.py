import threading
import time

def task():
    count = 0
    for _ in range(5 * 10**7):
        count += 1

start = time.time()

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

print("Multithreading:", time.time() - start)