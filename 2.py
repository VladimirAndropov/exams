import socket

# Создание клиентского сокета
cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключение к серверу
cli_socket.connect(('localhost', 8000))

# Отправка сообщения серверу
cli_socket.sendall(b"Hello, server!")

# Получение ответа от сервера
server_reply = cli_socket.recv(1024)
print("Server replied:", server_reply.decode())

# Закрытие сокета
cli_socket.close()
