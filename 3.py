import threading
import requests
import sys

def load_url(url):
    try:
        response = requests.get(url)
        print(f"Получена {url} с кодом ответа {response.status_code}")
    except Exception as e:
        print(f"Ошибка загрузки {url}: {e}")

def start_threads(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=load_url, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python downloader.py url1 url2 url3 ...")
        sys.exit(1)

    urls = sys.argv[1:]
    start_threads(urls)
