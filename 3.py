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

def main(urls):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # Запуск загрузки URL в параллельном режиме
        futures = [executor.submit(load_url, url) for url in urls]
        # Ожидание завершения всех задач
        for future in concurrent.futures.as_completed(futures):
            future.result()  # Получение результата задачи для обработки исключений

if __name__ == "__main__":
    # Проверка наличия аргументов командной строки
    if len(sys.argv) < 2:
        print("Usage: python downloader.py url1 url2 url3 ...")
        sys.exit(1)

    # Получение списка URL из аргументов командной строки
    urls = sys.argv[1:]

    # Запуск загрузки URL
    main(urls)
