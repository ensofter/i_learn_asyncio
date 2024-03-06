import socket
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level='DEBUG')
logger = logging.getLogger(__name__)

HOST = ('localhost', 10000)


def main():
    logger.info('Пишем клиентский сокет')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    logger.info('Коннектимся к нашему серверу')
    client.connect(HOST)

    logger.info('Получаем ответ от сервера')
    msg = client.recv(1024)
    logger.info(f'Сервер пишет нам - {msg}')

    logger.info('Отправляем информацию на серве')
    client.sendall(b'Word UP! Beach!')
    client.close()



if __name__ == '__main__':
    main()
