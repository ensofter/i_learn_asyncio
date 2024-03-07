import logging
import socket


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level='DEBUG')
logger = logging.getLogger(__name__)

HOST = ('localhost', 1234)

def main():
    logger.info('Погнали клиент')
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.info('Создали сокет клиент AF_INET и SOCK_STREAM')
    c.connect(HOST)
    logger.info('Подключились к серверу')
    data = c.recv(1024)
    logger.info(f'Приняли сообщение {data.decode("utf-8")}')


if __name__ == '__main__':
    main()
