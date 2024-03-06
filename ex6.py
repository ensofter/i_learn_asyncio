import json
import aiosqlite
import asyncio
from aiohttp import ClientSession, web
from aiologger.loggers.json import JsonLogger
from datetime import datetime


logger = JsonLogger.with_default_handlers(
    level='DEBUG',
    serializer_kwargs={'ensure_ascii': False}
)


async def create_table():
    async with aiosqlite.connect('weather.db') as db:
        await db.execute('CREATE TABLE IF NOT EXISTS requests '
                         '(date text, city text, weather text)')
        await db.commit()


async def save_to_db(city, weather):
    async with aiosqlite.connect('weather.db') as db:
        await db.execute('INSERT INTO requests VALUES (?, ?, ?)',
                         (datetime.now(), city, weather))
        await db.commit()


async def get_weather(city):
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            try:
                await logger.info(f"Мы получили ответ {weather_json['weather']}")
                return weather_json['weather'][0]['main']
            except KeyError:
                return 'Нет данных'

async def handle(request):
    city_ru = request.rel_url.query['city']

    await logger.info(f'Поступил запрос на город {city_ru}')

    weather = await get_weather(city_ru)

    result = {'city': city_ru, 'weather': weather}

    await save_to_db(city_ru, weather)

    return web.Response(text=json.dumps(result, ensure_ascii=False))


async def main():
    await create_table()
    app = web.Application()
    app.add_routes([web.get('/weather', handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()


    while True:
        await asyncio.sleep(3600)


if __name__ == '__main__':
    asyncio.run(main())
