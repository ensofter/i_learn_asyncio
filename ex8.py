import asyncio

from aiologger.loggers.json import JsonLogger


logger = JsonLogger.with_default_handlers(
    level='DEBUG',
    serializer_kwargs={'ensure_ascii':False}
)


async def main():
    await logger.info('запускаем асинхронную задачу')
    print('Запускаем асинхронную задачу')
    task = asyncio.create_task(asyncio.sleep(2))
    await task

if __name__ == '__main__':
    asyncio.run(main())
    print('Вышли из цикла событий')
