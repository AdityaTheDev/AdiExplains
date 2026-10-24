
import asyncio

async def get_profile():
    print("Fetching profile...")
    await asyncio.sleep(2)
    return {"name": "Adi"}

async def get_settings():
    print("Fetching settings...")
    await asyncio.sleep(2)
    return {"theme": "dark"}

async def main():
    profile_task = asyncio.create_task(get_profile())
    settings_task = asyncio.create_task(get_settings())

    # Both operations have already been scheduled.
    profile = await profile_task
    settings = await settings_task

    print(profile, settings)

asyncio.run(main())
