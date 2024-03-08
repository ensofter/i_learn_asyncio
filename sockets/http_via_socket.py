import logging
import socket


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level='DEBUG')
logger = logging.getLogger(__name__)

HOST = ('example.com', 80)


def parse_http_response(text_response: str):
    lines = text_response.split('\n')
    status_raw, lines = lines[0], lines[1:]
    protocol, status_code, message = status_raw.split(' ')
    empty_index = 1
    headers = {}
    for index, line in enumerate(lines):
        line = line.strip().strip('\r')
        if line == '':
            empty_index = index
            break
        print(line)
        k, _, v = line.partition(':')
        headers.setdefault(k.strip(), v.strip())
    content = ''.join(lines[empty_index + 1:])
    return int(status_code), headers, content


def main():
    logger.info('Пишем аналог того как работает протокол http на транспортном уровне протокола TPC')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.info(f'Создали сокет клиента {s}')
    s.connect(HOST)
    logger.info(f'Приконектились к хосту {HOST}')
    content_items = [
        'GET / HTTP/1.1',
        'Host: example.com',
        'Connection: keep-alive',
        'Accept: text/html',
        '\n'
    ]
    logger.info(f'Подготовили запрос {content_items}')
    content = '\n'.join(content_items)
    logger.info(f'Объединили все в одну строку {content}')
    print('--- HTTP MESSAGE ---')
    print(content)
    print('--- END OF MESSAGE ---')
    s.send(content.encode())
    logger.info('Отправили запрос')
    response = s.recv(10024)
    logger.info(f'Получили ответ {response}')
    status_code, headers, content = parse_http_response(response.decode())
    logger.info(f'status_code: {status_code}')
    logger.info(f'headers: {headers}')
    logger.info(f'content: {content}')


if __name__ == '__main__':
    main()
