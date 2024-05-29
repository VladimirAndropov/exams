import sys
import requests

def fetch_content_from_url(url):
    try:
        # Отправляем GET-запрос по указанному URL
        response = requests.get(url)

        # Проверяем успешность запроса
        if response.status_code == 200:
            # Выводим тело ответа
            print(response.text)
        else:
            print(f"Ошибка: получен код состояния {response.status_code}")
    except requests.RequestException as error:
        print(f"Произошла ошибка при выполнении запроса: {error}")

if __name__ == "__main__":
    # Проверяем, что передан ровно один аргумент командной строки
    if len(sys.argv) != 2:
        print("Usage: python 4.py <URL>")
        sys.exit(1)

    # Извлекаем URL из аргументов командной строки
    url_to_fetch = sys.argv[1]

    # Получаем и выводим содержимое по указанному URL
    fetch_content_from_url(url_to_fetch)
