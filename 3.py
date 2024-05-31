import threading
import requests
import sys


def fetch_url(url):
    try:
        response = requests.get(url)
        print(f"URL: {url}, Status Code: {response.status_code}")
    except Exception as e:
        print(f"URL: {url}, Error: {str(e)}")


def main(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print("Please provide a list of URLs as arguments.")
