import sys
import aiohttp
import asyncio

async def async_http_client(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                # Проверка статуса ответа
                if response.status == 200:
                    # Вывод тела ответа на терминал
                    print("Response Body:")
                    print(await response.text())
                else:
                    print(f"Failed to fetch URL: {response.status}")
    except aiohttp.ClientError as e:
        print(f"Error fetching URL: {e}")

if __name__ == "__main__":
    # Проверка наличия аргумента командной строки (URL)
    if len(sys.argv) != 2:
        print("Usage: python http_client.py <URL>")
        sys.exit(1)

    # Получение URL из аргумента командной строки
    url = sys.argv[1]

    # Запуск асинхронной функции для отправки запроса и вывода ответа
    asyncio.run(async_http_client(url))
