import threading
import time

balance = 10000
lock = threading.Lock()


def withdraw(amount):
    global balance

    print(f"{threading.current_thread().name} checking balance")
    try:
        with lock:
            if balance >= amount:
                time.sleep(1)
                balance -= amount
                print(f"Withdrawn: {amount}")
            else:
                print(f"Insufficient balance while {threading.current_thread().name} trying to withdraw {amount}")
    except Exception as e:
        print(e)



t1 = threading.Thread(
    target=withdraw, args=(7000,), name="Thread-1"
)

t2 = threading.Thread(
    target=withdraw, args=(5000,), name="Thread-2"
)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Balance:", balance)