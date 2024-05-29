import threading
import requests
import sys

def fetch_url(url):
    try:
        response = requests.get(url)
        print(f"Successfully fetched {url} with status {response.status_code}")
    except Exception as err:
        print(f"Failed to fetch {url}: {err}")

def initiate_threads(url_list):
    thread_list = []
    for url in url_list:
        t = threading.Thread(target=fetch_url, args=(url,))
        thread_list.append(t)
        t.start()
    for t in thread_list:
        t.join()

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python downloader.py <url1> <url2> <url3> ...")
        sys.exit(1)

    url_list = sys.argv[1:]

    initiate_threads(url_list)
