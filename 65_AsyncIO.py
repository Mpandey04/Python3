import asyncio
# async def task():
#     await asyncio.sleep(2)
#     print("Done")

# async def main():
#     t = asyncio.create_task(task())

#     print("Doing something else")

#     await t

# asyncio.run(main())

async def fetch_data(name, delay):
    print(f"Fetching {name}...")
    await asyncio.sleep(delay)  # Simulate network delay
    print(f"{name} received")
    return f"Data from {name}"

async def main():
    results = await asyncio.gather(
        fetch_data("API 1", 2),
        fetch_data("API 2", 1),
        fetch_data("API 3", 3),
    )

    print("\nResults:")
    for result in results:
        print(result)

asyncio.run(main())