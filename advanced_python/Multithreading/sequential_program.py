import time
from time import perf_counter

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

cook_dosa()
cook_fried_rice()
cook_noodles()

end = perf_counter()
print(f"Total time taken: {end - start:.2f} seconds")