import pickle
import logging
import socket


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(message)s', level='DEBUG')
logger = logging.getLogger(__name__)

HOST = ('localhost', 12345)

def main():
    logger.info('Создаем сокет')
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.info('Коннектим его к серверу')
    c.connect(HOST)

    resp = c.recv(4096)
    logger.info(f'Получили от вет от сервера {resp}')
    deserialize_str = pickle.loads(resp)
    logger.info(f'Десериализовали полученную байт строку {deserialize_str}')

if __name__ == '__main__':
    main()
