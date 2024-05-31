import threading
import requests
import sys

# Функция для загрузки URL
def load_url(url):
    try:
        response = requests.get(url)
        print(f"Loaded {url} with status code {response.status_code}")
    except Exception as e:
        print(f"Error loading {url}: {e}")

# Функция для создания и запуска потоков для загрузки URL
def start_threads(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=load_url, args=(url,))
        threads.append(thread)
        thread.start()
    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Проверка наличия аргументов командной строки
    if len(sys.argv) < 2:
        print("Usage: python downloader.py url1 url2 url3 ...")
        sys.exit(1)

    # Получение списка URL из аргументов командной строки
    urls = sys.argv[1:]

    # Запуск загрузки URL в многопоточном режиме
    start_threads(urls)
