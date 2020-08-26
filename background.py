import os
import requests
from time import sleep
import logging
import file_generator

LOG_FILENAME = 'error.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.WARNING)

PROCESSED_FOLDER_NAME = 'processed'

url = 'http://back:8000/agent/upload/'


def agent():
    file_generator.main()  # для тестирования вначале добавляется один файл
    while True:
        for fname in os.listdir('.'):
            if fname.endswith('.test'):
                f = open(fname, 'rb')
                files = {'file': f}
                try:
                    requests.post(url=url, files=files)
                except requests.RequestException as e:
                    logging.warning(f'Server Error: {e}')
                    break
                finally:
                    f.close()
                os.replace(fname, f'{PROCESSED_FOLDER_NAME}/{fname}')
        sleep(60)


def main():
    agent()


if __name__ == '__main__':
    main()
