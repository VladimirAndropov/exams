import concurrent.futures
import requests
import sys

# Функция для загрузки URL
def load_url(url):
    try:
        response = requests.get(url)
        print(f"Loaded {url} with status code {response.status_code}")
    except Exception as e:
        print(f"Error loading {url}: {e}")

if __name__ == "__main__":
    # Проверка наличия аргументов командной строки
    if len(sys.argv) < 2:
        print("Usage: python downloader.py url1 url2 url3 ...")
        sys.exit(1)

    # Получение списка URL из аргументов командной строки
    urls = sys.argv[1:]

    # Создание пула потоков с максимальным количеством равным количеству URL
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(urls)) as executor:
        # Подача задач на загрузку URL в пул потоков
        futures = [executor.submit(load_url, url) for url in urls]
        # Ожидание завершения всех задач
        concurrent.futures.wait(futures)
