# A parking lot has 3 spaces, but 6 cars arrive at the same time.

import threading
import time



def car(name):
    print(name, "waiting...")

    print(name, "PARKED")
    time.sleep(2)          # the car stays parked for 2 seconds
    
    print(name, "LEFT")


start = time.time()
threads = []

# Create 6 threads, one for each car, and start them all at once.
for i in range(1, 7):
    t = threading.Thread(target=car, args=(f"Car-{i}",))
    t.start()
    threads.append(t)

# Wait until every car has left before printing the total time.
for t in threads:
    t.join()

# 6 cars, 3 spaces, 2 seconds each = 2 rounds = about 4 seconds.
print(f"Total time: {time.time() - start:.1f} seconds")