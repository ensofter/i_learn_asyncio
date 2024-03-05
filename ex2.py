import asyncio


async def get_conn(host, port):

    class Conn:
        async def put_data(self):
            print('Отправка данных...')
            await asyncio.sleep(2)
            print('Данные отправлены')


        async def get_data(self):
            print('Получение данных...')
            await asyncio.sleep(2)
            print('Данные получены')


        async def close(self):
            print('Завершение соединения....')
            await asyncio.sleep(2)
            print('Соединение закрыто')


    print('Устанавливаем соединение')
    await asyncio.sleep(2)
    print('Соединение установленно.')
    return Conn()


class Connection:
    # этот конструктор будуе выполнен в заголовке with
    def __init__(self, host, port):
        self.host = host
        self.port = port

    # этот метод будет неявно выполнен при входе в with
    async def __aenter__(self):
        self.conn = await get_conn(self.host, self.port)
        return self.conn

    # жтот метод будет неявно выполнен при выходе из with
    async def __aexit__(self, exc_type, exc, tb):
        await self.conn.close()


async def main():
    async with Connection('localhost', 9001) as conn:
        send_task = asyncio.create_task(conn.put_data())
        recieve_task = asyncio.create_task(conn.get_data())

        await send_task
        await recieve_task

if __name__ == '__main__':
    asyncio.run(main())
