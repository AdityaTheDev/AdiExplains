import threading
import time

balance = 1000

def withdraw(name, amount):
    global balance

    print(f"{name} checking balance... {balance}")

    if balance >= amount:
        temp = balance
        time.sleep(1)   #orce both threads to pause here
        temp -= amount
        balance = temp

        print(f"{name} withdrew {amount}")

    else:
        print(f"{name} insufficient balance")

t1 = threading.Thread(target=withdraw, args=("Person A", 600))
t2 = threading.Thread(target=withdraw, args=("Person B", 500))

t1.start()
t2.start()

t1.join()
t2.join()

print("Final balance:", balance)