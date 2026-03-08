import time
from time import perf_counter

import threading

start = perf_counter()

def cook_dosa():
    print("Cooking dosa...")
    time.sleep(5)
    print("Dosa ready")

def cook_fried_rice():
    print("Cooking fried rice...")
    time.sleep(7)
    print("Fried rice ready")

def cook_noodles():
    print("Cooking noodles...")
    time.sleep(6)
    print("Noodles ready")

t1= threading.Thread(target=cook_dosa)
t2 = threading.Thread(target=cook_fried_rice)
t3= threading.Thread(target=cook_noodles)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end = perf_counter()
print(f"Total time taken: {end - start:.2f} seconds")




























# import time
# from concurrent.futures import ThreadPoolExecutor
# from time import perf_counter

# start = perf_counter()

# def cook_dosa():
#     print("Cooking dosa...")
#     time.sleep(5)
#     print("Dosa ready")

# def cook_fried_rice():
#     print("Cooking fried rice...")
#     time.sleep(7)
#     print("Fried rice ready")

# def cook_noodles():
#     print("Cooking noodles...")
#     time.sleep(6)
#     print("Noodles ready")

# with ThreadPoolExecutor() as executor:
#     executor.submit(cook_dosa)
#     executor.submit(cook_fried_rice)
#     executor.submit(cook_noodles)

# end = perf_counter()
# print(f"Total time taken: {end - start:.2f} seconds")