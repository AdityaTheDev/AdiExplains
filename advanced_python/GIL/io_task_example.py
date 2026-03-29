import threading
import time

def task():
    time.sleep(2)  # Simulating a time-consuming task
    print("Done")

start = time.time()

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

print("Time:", time.time() - start)