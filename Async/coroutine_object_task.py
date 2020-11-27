import asyncio
import time

async def say_after(delay, what):
    print(f"run say_after at {time.strftime('%X')}")
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    task = asyncio.create_task(say_after(5, 'hello'))
    print('created co_obj')

    await asyncio.sleep(3)
    print(f"sleeped finish at {time.strftime('%X')}")

    print('start await co_obj')
    await task

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())