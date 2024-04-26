# Напишите простой многопоточный загрузчик URL. Список URL скрипт принимает как аргументы командной строки.

import sys
import threading
import requests

def download_url(url):
    print(f"Скачивание {url}")
    response = requests.get(url)
    print(f"Завершено {url}: {response.status_code}")

for url in sys.argv[1:]:
    thread = threading.Thread(target=download_url, args=(url,))
    thread.start()
