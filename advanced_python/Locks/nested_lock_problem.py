import threading

lock = threading.RLock()


def check_balance():
    with lock:
        print("Checking account balance")


def withdraw():
    with lock:
        print("Starting withdrawal")

        check_balance()

        print("Withdrawal completed")


withdraw()