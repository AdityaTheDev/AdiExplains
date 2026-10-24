import time
from time import perf_counter

def fetch_data(name):
    print(f"Fetching {name}")
    time.sleep(2) 
    print(f"Completed {name}")

start_time = perf_counter()
fetch_data("API 1")
fetch_data("API 2")
fetch_data("API 3")
end_time = perf_counter()
print(f"Total time taken: {end_time - start_time} seconds")