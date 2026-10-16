import json

import requests


def calculate_total(price, quantity, discount=0):
    subtotal = price * quantity
    discount_amount = subtotal * discount
    total = subtotal - discount_amount
    return total


def get_user_data(user_id):
    url = "https://jsonplaceholder.typicode.com/users/" + str(user_id)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


class UserManager:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.users = []
        self.cache = {}

    def add_user(self, name, email, age):
        user = {"name": name, "email": email, "age": age}
        self.users.append(user)
        return user

    def find_user(self, email):
        for user in self.users:
            if user["email"] == email:
                return user
        return None

    def delete_user(self, email):
        for user in self.users:
            if user["email"] == email:
                self.users.remove(user)
                return True
        return False


def process_users(users):
    results = []
    for user in users:
        if user.get("age", 0) > 18 and user.get("email") and "@" in user["email"]:
            result = {"name": user["name"], "email": user["email"], "adult": True}
            results.append(result)
    return results


def save_users(users, filename="users.json"):
    with open(filename, "w") as file:
        json.dump(users, file, indent=4)


def load_users(filename="users.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []


def generate_report(users):
    print("====================================")
    print("USER REPORT")
    print("====================================")

    total_users = len(users)
    adult_users = 0
    total_age = 0

    for user in users:
        total_age += user.get("age", 0)
        if user.get("age", 0) >= 18:
            adult_users += 1

    if total_users > 0:
        average_age = total_age / total_users
    else:
        average_age = 0

    print("Total users:", total_users)
    print("Adults:", adult_users)
    print("Average age:", average_age)


def main():
    users = [
        {"name": "John", "email": "john@example.com", "age": 25},
        {"name": "Alice", "email": "alice@example.com", "age": 17},
        {"name": "Bob", "email": "bob@example.com", "age": 32},
        {"name": "Charlie", "email": "charlie@example.com", "age": 19},
    ]

    processed = process_users(users)

    save_users(processed)

    loaded = load_users()

    generate_report(loaded)

    total = calculate_total(100, 5, 0.1)
    print("Total:", total)


if __name__ == "__main__":
    main()
