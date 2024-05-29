import threading
import requests
import sys

# Функция для загрузки URL
def download_url(url):
    try:
        response = requests.get(url)
        print(f"URL: {url} - Status: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Функция для инициации и запуска потоков
def start_downloads(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_url, args=(url,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

# Основная часть скрипта
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python 3.py <url1> <url2> <url3> ...")
        sys.exit(1)

    urls = sys.argv[1:]
    start_downloads(urls)
