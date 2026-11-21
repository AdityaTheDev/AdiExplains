# Practice solution: 2 ATMs, 6 customers, 3 seconds each.
# Expected total time: about 9 seconds (6 customers / 2 at a time = 3 rounds x 3 s).

import threading
import time

semaphore = threading.Semaphore(2)  # 2 ATMs available

def customer(name):
    print(name, "is in the queue")
    with semaphore:
        print(name, "started using an ATM")
        time.sleep(3)          # using the ATM takes 3 seconds
        print(name, "finished")


start = time.time()
threads = []

for i in range(1, 7):
    t = threading.Thread(target=customer, args=(f"Customer-{i}",))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"Total time: {time.time() - start:.1f} seconds")