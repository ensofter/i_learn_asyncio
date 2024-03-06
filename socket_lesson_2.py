import socket
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level='DEBUG')
logger = logging.getLogger(__name__)


HOST = ('localhost', 10000)

def main():
    logger.info('Погнали')
    logger.info('Создаем сокет TCP/IP')
    s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.info('Биндим сокет к нашему эндпойнту Хост + порт')
    s_server.bind(HOST)
    logger.info('Ставим сокет на прослушку')
    s_server.listen()

    print("I'm lostening your connection")
    logger.info('Ожидаем входящие подключения')
    while True:
        logger.info('Принимаем входящее подключение')
        conn, addr = s_server.accept()
        logger.info(f'Connected - {addr}')
        response = b'Hello, my friend'
        logger.info(f'Отправляем сообщение клиенту {response}')
        conn.send(response)
        logger.info('Принимаем информацию от клиента')
        msg = conn.recv(1024)
        logger.info(f'Вот такое сообщение {msg}')
        logger.info('Закрываем сеанс соединения')
        conn.close()


if __name__ == '__main__':
    main()

