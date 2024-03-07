import logging
import socket
import pickle


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level='DEBUG')
logger = logging.getLogger(__name__)

HOST = ('localhost', 12345)

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.info(f'Создали сокет {s}')
    s.bind(HOST)
    logger.info('Забиндили сокет')
    s.listen(1)
    logger.info('Начинаем прослушку')

    d = {'name': 'Alex', 'age': 20}
    logger.info(f'формируем данные для передачи {d}')
    while True:
        conn, addr = s.accept()
        logger.info(f'Принято соединение с {addr}')
        resp = pickle.dumps(d)
        logger.info(f'Запиклили словарь {resp}')
        conn.send(resp)
        logger.info('Отправили клиенту байт строку')
        conn.close()

if __name__ == '__main__':
    main()
