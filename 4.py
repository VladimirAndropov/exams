import sys
import requests

def simple_http_client(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Тело:")
            print(response.text)
        else:
            print(f"Ошибка получения данных по эндпоинту (код): {response.status_code}")
    except requests.RequestException as e:
        print(f"Ошибка получения данных по эндпоинту: {e}")

if len(sys.argv) != 2:
    print("Usage: python http_client.py <URL>")
    sys.exit(1)
url = sys.argv[1]
simple_http_client(url)
