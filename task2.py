import socket

# Создание сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

# Установка неблокирующего режима для сокета
server_socket.setblocking(False)

print("Эхо-сервер запущен.")

# Список подключенных клиентов
clients = []

while True:
    try:
        # Принятие нового подключения
        client_socket, addr = server_socket.accept()
        client_socket.setblocking(False)
        clients.append(client_socket)
        print("Подключился клиент:", addr)
    except socket.error:
        pass

    # Чтение данных от клиентов
    for client_socket in clients:
        try:
            data = client_socket.recv(1024)
            if data:
                print("Получено от", client_socket.getpeername(), ":", data.decode())
                client_socket.sendall(data)
            else:
                print("Клиент", client_socket.getpeername(), "отключился.")
                client_socket.close()
                clients.remove(client_socket)
        except socket.error:
            pass
