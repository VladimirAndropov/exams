import sys
import requests


def fetch_url_content(url):
    try:
        # Выполнение GET-запроса к указанному URL
        response = requests.get(url)

        # Проверка успешности запроса
        if response.status_code == 200:
            # Печать тела ответа
            print("Тело ответа:")
            print(response.text)
        else:
            print(f"Не удалось получить данные с URL: Код ошибки {response.status_code}")
    except requests.RequestException as error:
        print(f"Произошла ошибка при выполнении запроса: {error}")


if __name__ == "__main__":
    # Проверка наличия необходимого аргумента командной строки (URL)
    if len(sys.argv) != 2:
        print("Использование: python http_client.py <URL>")
        sys.exit(1)

    # Извлечение URL из аргумента командной строки
    url = sys.argv[1]

    # Вызов функции для получения содержимого по указанному URL
    fetch_url_content(url)
