import socket
import logging

logging.basicConfig(format='%(asctime)s – %(module)s – %(levelname)s: %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)

def main():
    logger.info('Создаем сокет')
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    logger.info('Подключаемся к серверу')
    client_socket.connect(('localhost', 12345))

    logger.info('Отправляем данные серверу')
    client_socket.sendall(b'Helol world!')

    logger.info('Закрываем соединение')
    client_socket.close()

if __name__ == "__main__":
    main()
