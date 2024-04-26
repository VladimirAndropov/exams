# Напишите простой эхо-сервер, использующий неблокирующие сокеты и клиент к нему.

import socket
import threading


def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.sendall(data)
    client_socket.close()


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ("localhost", 12345)
    tcp_socket.bind(server_address)

    tcp_socket.listen(5)

    while True:
        client_socket, client_address = tcp_socket.accept()

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


if __name__ == "__main__":
    main()
