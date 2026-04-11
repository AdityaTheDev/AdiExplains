import requests
import time

URL = "https://randomuser.me/api/"

def fetch_user():
    response = requests.get(URL)
    data = response.json()
    name = data["results"][0]["name"]["first"]
    return name

start = time.time()

for _ in range(14):
    print(fetch_user())

end = time.time()

print(f"\nTotal time (sync): {end - start:.2f} seconds")

# It took 8.38 seconds to fetch 14 users sequentially. This is because each request waits for the previous one to complete before starting, leading to a cumulative delay.