import socket
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level='DEBUG')
logger = logging.getLogger(__name__)

HOST = ('localhost', 1234)


def main():
    logger.info('Погнали')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.info('Создали сокет AF_INET и SOCK_STREAM')
    s.bind(HOST)
    s.listen(1)
    logger.info('Слушаем...')
    while True:
        conn, addr = s.accept()
        logger.info(f'К нам подключился клиент {addr}')
        msg = 'Привет заебал!'.encode('utf-8')
        conn.send(msg)
        logger.info(f'Отправили сообщение {msg}')
        conn.close()



if __name__ == "__main__":
    main()
