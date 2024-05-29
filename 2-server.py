import socket
import select

# Настройки сервера
server_host = 'localhost'
server_port = 8000

# Создание сокета
srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv_socket.bind((server_host, server_port))
srv_socket.listen(5)
srv_socket.setblocking(0)

# Списки сокетов для работы с select
socket_list = [srv_socket]

try:
    while True:
        readable, _, exceptional = select.select(socket_list, [], socket_list)
        
        for s in readable:
            if s is srv_socket:
                # Обработка нового входящего подключения
                client_socket, client_address = s.accept()
                client_socket.setblocking(0)
                socket_list.append(client_socket)
            else:
                # Чтение данных от клиента
                message = s.recv(1024)
                if message:
                    s.sendall(message)
                else:
                    socket_list.remove(s)
                    s.close()

        for s in exceptional:
            socket_list.remove(s)
            s.close()

except KeyboardInterrupt:
    srv_socket.close()
