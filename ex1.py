import asyncio
import time


async def func1(n: int):
    print(n**4)
    await asyncio.sleep(3)
    print('func1 завершена')


async def func2(n: int):
    print(n**0.5)
    await asyncio.sleep(3)
    print('func2 завершена')


async def main():

    task1 = asyncio.create_task(func1(4))
    task2 = asyncio.create_task(func2(4))

    await task1
    await task2


if __name__ == '__main__':
    asyncio.run(main())
