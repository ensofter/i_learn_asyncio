import logging
import socket
from asyncio import AbstractEventLoop
import asyncio

logging.basicConfig(format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s', level='DEBUG')
logger = logging.getLogger('asyncio')

HOST = ('localhost', 12345)

async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    logger.info('Используем низкоуровневые функции цикла событий')
    while data := await loop.sock_recv(connection, 1024):
        logger.info(f'Получен данные {data}')
        await loop.sock_sendall(connection, data)

async def listen_for_connection(server_socket: socket, loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        logger.info(f'Получен запрос на соединение от {address}')
        asyncio.create_task(echo(connection, loop))

async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.setblocking(False)
    server_socket.bind(HOST)
    server_socket.listen()

    logger.info('Извлекаем цикл событий')
    asyncio_loop = asyncio.get_event_loop()

    await listen_for_connection(server_socket, asyncio_loop)


if __name__ == '__main__':
    asyncio.run(main())


