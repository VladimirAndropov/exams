import sys
import requests

def simple_http_client(url):
    try:
        # Отправка GET-запроса по указанному URL
        response = requests.get(url)

        # Проверка статуса ответа
        if response.status_code == 200:
            # Вывод тела ответа на терминал
            print("Response Body:")
            print(response.text)
        else:
            print(f"Failed to fetch URL: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")

if __name__ == "__main__":
    # Проверка наличия аргумента командной строки (URL)
    if len(sys.argv) != 2:
        print("Usage: python http_client.py <URL>")
        sys.exit(1)

    # Получение URL из аргумента командной строки
    url = sys.argv[1]

    # Вызов функции для отправки запроса и вывода ответа
    simple_http_client(url)
