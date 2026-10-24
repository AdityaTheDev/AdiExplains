
import asyncio

async def get_user():
    await asyncio.sleep(1)
    return {
        "id": 101,
        "preferences": ["Python", "AI"]
    }

async def get_orders(user_id):
    await asyncio.sleep(2)
    return [f"Orders for {user_id}"]

async def get_recommendations(preferences):
    await asyncio.sleep(2)
    return [f"Recommendations for {preferences}"]

async def main():
    # Step 1: Must finish first.
    user = await get_user()

    # Step 2: These can now run concurrently.
    orders_task = asyncio.create_task(
        get_orders(user["id"])
    )
    recommendations_task = asyncio.create_task(
        get_recommendations(user["preferences"])
    )

    orders = await orders_task
    recommendations = await recommendations_task

    print(orders)
    print(recommendations)

asyncio.run(main())
