import socket
import logging


logging.basicConfig(format='%(asctime)s - %(module)s - %(levelname)s: %(message)s', level=logging.DEBUG)


logger = logging.getLogger(__name__)

def main():
    logger.info('Создаем сокет')
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.info('Привязываем сокет к IP-адресу и порту')
    server_socket.bind(('localhost', 12345))
    logger.info('Слушаем соединение')
    server_socket.listen(1)

    print('Сервер запущен и ожидает подключений...')

    logger.info('Принимаем входящее соединение')

    client_socket, client_address = server_socket.accept()
    print(f'Подключение установлено с {client_address}')

    logger.info('Получаем данные от клиента')
    data = client_socket.recv(1024)
    print(f'Получены данные: {data}')

    logger.info('Закрываем соединение')
    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    main()
