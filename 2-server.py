import socket

# Создание сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Установка опции сокета для неблокирующего режима
server_socket.setblocking(False)

# Привязка сокета к адресу и порту
server_socket.bind(('localhost', 8888))

# Прослушивание подключений
server_socket.listen(5)
print("Server is listening...")

# Список подключенных клиентов
clients = []

# Функция для обработки входящих соединений и данных
def handle_connections():
    while True:
        # Принятие входящего соединения
        try:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")
            # Добавление клиента в список
            clients.append(client_socket)
        except BlockingIOError:
            pass

        # Обработка входящих данных от клиентов
        for client in clients:
            try:
                data = client.recv(1024)
                if data:
                    print(f"Received: {data.decode()}")
                    # Отправка обратно данных клиенту
                    client.sendall(data)
                else:
                    # Если клиент закрыл соединение, удаляем его из списка
                    clients.remove(client)
                    client.close()
            except BlockingIOError:
                pass

# Запуск функции для обработки соединений в отдельном потоке
import threading
threading.Thread(target=handle_connections).start()
