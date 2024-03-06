import asyncio


async def get_message():
    await asyncio.sleep(2)
    print('hello server')


async def listen_port():
    while True:
        await asyncio.sleep(5)
        print('request received for connection, waiting message')
        asyncio.create_task(get_message())


async def main():
    await asyncio.create_task(listen_port())


if __name__ == '__main__':
    asyncio.run(main())
