import socket
import select


# Echo server
def echo_server(host='localhost', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setblocking(False)
    server_socket.bind((host, port))
    server_socket.listen(5)

    inputs = [server_socket]
    outputs = []

    while inputs:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)
        for s in readable:
            if s is server_socket:
                connection, client_address = s.accept()
                connection.setblocking(False)
                inputs.append(connection)
            else:
                data = s.recv(1024)
                if data:
                    s.send(data)
                else:
                    inputs.remove(s)
                    s.close()


# Echo client
def echo_client(host='localhost', port=65432, message='Hello, server!'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(message.encode())
        data = s.recv(1024)
        print('Received', repr(data))


# echo_server()


# echo_client()
