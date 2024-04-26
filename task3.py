import sys
import threading
import requests

# Функция для загрузки URL
def download_url(url):
    try:
        response = requests.get(url)
        print("Скачано: {} - {}".format(url, len(response.content)))
    except Exception as e:
        print("Ошибка при загрузке {}: {}".format(url, e))

if __name__ == "__main__":
    # Получение списка URL из аргументов командной строки
    urls = sys.argv[1:]

    # Создание потоков для загрузки каждого URL
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_url, args=(url,))
        threads.append(thread)
        thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    print("Все загрузки завершены.")
