import threading


class Restaurant:

    def __init__(self):
        self.customer_orders: dict[int,list[str]] = {}
        self.lock = threading.RLock()

    def check_customer_order(self, customer_id: int, food_item: str) -> bool:

        with self.lock:
            print(f"Checking order for customer {customer_id}")

            return food_item in self.customer_orders.get(customer_id, [])

    def place_order(self, customer_id: int, food_item: str):

        with self.lock:
            print(f"Placing order for customer {customer_id}")

            #Nested method call using the same RLock
            if not self.check_customer_order(customer_id, food_item):

                self.customer_orders.setdefault(customer_id, []).append(food_item)

                print(f"{food_item} added successfully!")

            else:
                print(f"{food_item} already ordered by customer {customer_id}")


# Create restaurant
restaurant = Restaurant()

# Place orders
restaurant.place_order(101, "Pizza")
restaurant.place_order(101, "Burger")
restaurant.place_order(102, "Pizza")
restaurant.place_order(101, "Pizza")

print("\nFinal Orders:")
print(restaurant.customer_orders)