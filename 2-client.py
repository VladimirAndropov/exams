import socket

# Создание клиентского сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключение к серверу
client_socket.connect(('localhost', 8888))

# Отправка данных серверу
message = "Hello, Server, bye!"
client_socket.sendall(message.encode())

# Получение данных от сервера
data = client_socket.recv(1024)
print(f"Echo from server: {data.decode()}")

# Закрытие соединения
client_socket.close()

