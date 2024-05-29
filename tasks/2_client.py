import socket

# Адрес сервера
server_address = ('localhost', 8888)

# Создание клиентского сокета и подключение к серверу
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
    client_sock.connect(server_address)
    client_sock.sendall(b'Hello, Echo Server!')
    reply = client_sock.recv(1024)
    print('Received:', reply.decode())
