import socket
import logging


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(message)s', level='DEBUG')
logger = logging.getLogger(__name__)


HOST = ('localhost', 1234)

def main():
    logger.info('Пишем клиента который отправляет GET запрос')

    logger.info('Создаем сокет на базе TCP_IP')
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.info(f'Коннектим сокет с хостом {HOST}')
    c_socket.connect(HOST)
    msg = b'GET / HTTP/1.1\r\nHOST:localhost:1234\r\n\r\n'
    logger.info(f'Отправляем GET запрос {msg}')
    c_socket.send(msg)



if __name__ == '__main__':
    main()
