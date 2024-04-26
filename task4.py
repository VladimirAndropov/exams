import sys
import requests

def simple_http_client(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Тело ответа:")
            print(response.text)
        else:
            print("Ошибка: Статус код", response.status_code)
    except requests.RequestException as e:
        print("Ошибка при выполнении запроса:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python http_client.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    simple_http_client(url)
