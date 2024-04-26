# Напишите простой эхо-сервер, использующий неблокирующие сокеты и клиент к нему.

# Сервер 

import socket
import select

host = 'localhost'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
server_socket.setblocking(0)

inputs = [server_socket]
outputs = []

try:
    while inputs:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)

        for s in readable:
            if s is server_socket:
                connection, client_address = s.accept()
                connection.setblocking(0)
                inputs.append(connection)
            else:
                data = s.recv(1024)
                if data:
                    s.send(data)
                else:
                    inputs.remove(s)
                    s.close()
except KeyboardInterrupt:
    server_socket.close()

# Клиент

import socket

host = 'localhost'
port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b'hi')
    data = s.recv(1024)
    print('Ответ:', data.decode())
