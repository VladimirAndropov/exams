import socket

# Создание сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключение к серверу
client_socket.connect(('localhost', 8888))

# Отправка данных серверу
client_socket.sendall(b"Hello, server!")

# Получение данных от сервера
data = client_socket.recv(1024)
print("Received from server:", data.decode())

# Закрытие соединения
client_socket.close()