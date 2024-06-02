'''3. Напишите простой многопоточный загрузчик URL. Список URL скрипт принимает как аргументы командной строки.'''

import threading
import requests
import sys


# Функция для загрузки URL и обработки ответа
def fetch_url(url):
    try:
        result = requests.get(url)
        print(f"URL: {url} | Status: {result.status_code}")
    except requests.RequestException as error:
        print(f"Failed to fetch {url}: {error}")


# Функция для создания и управления потоками
def initiate_threads(url_list):
    thread_list = []
    for url in url_list:
        t = threading.Thread(target=fetch_url, args=(url,))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python 3.py <url1> <url2> ...")
        sys.exit(1)

    # Извлечение URL из аргументов командной строки
    url_list = sys.argv[1:]

    # Запуск потоков для загрузки URL
    initiate_threads(url_list)

'''
juliamekhtieva@MacBook-Pro-73 exam_net_sys % python 3.py http://example.com http://example.org http://example.net
URL: http://example.com | Status: 200
URL: http://example.org | Status: 200
URL: http://example.net | Status: 200
'''