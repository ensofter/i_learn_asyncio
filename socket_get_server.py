import logging
import socket


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(message)s', level='DEBUG')
logger = logging.getLogger(__name__)


HOST = ('localhost', 1234)

def main():
    logger.info('Создаем сокет серве на базе AF_INET и SOCK_STREAM')
    s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.info(f'Биндим сервер к хосту {HOST}')
    s_server.bind(HOST)
    s_server.listen(1)

    while True:
        logger.info('Принимаем входящее соединение')
        conn, addr = s_server.accept()
        logger.info(f'К нам подключился {conn} с адресом {addr}')

        req = ''
        while True:
            logger.info('Ждем запрос')
            data = conn.recv(4096)
            if not len(data):
                break
            logger.info(f'Получили кусок данных {data}')
            req += data.decode()


        logger.info('Закрыаем соединение с клиентом')
        conn.close()


if __name__ == '__main__':
    main()
