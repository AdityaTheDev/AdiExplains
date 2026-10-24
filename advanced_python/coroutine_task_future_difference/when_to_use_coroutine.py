
import asyncio

async def get_user():
    print("Fetching user...")
    await asyncio.sleep(1)
    print("User received")
    return {"id": 101, "name": "Adi"}

async def get_orders(user_id):
    print(f"Fetching orders for user {user_id}...")
    await asyncio.sleep(1)
    if user_id == 101:
        return ["Laptop", "Keyboard"]
    else:
        return []

async def main():

    user = await get_user()
    #We need the user ID before this call.
    orders = await get_orders(user["id"])

    print(orders)

asyncio.run(main())
