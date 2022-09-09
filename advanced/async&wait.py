# async,await

import asyncio


async def function(i):
    print(f"Hello, function {i} started")
    await asyncio.sleep(4)
    print(f"Hello function {i} has been completed")


async def main():
    task1 = asyncio.create_task(function(1))
    await asyncio.sleep(2)
    task2 = asyncio.create_task(function(2))
    await asyncio.sleep(2)
    task3 = asyncio.create_task(function(3))
    await task1
    await task2
    await task3


asyncio.run(main())
