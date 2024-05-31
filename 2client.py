import socket

# Создание сокета клиента
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключение к серверу
client_socket.connect(('localhost', 8888))

while True:
    message = input("Enter message to send: ")
    client_socket.sendall(message.encode())

    # Получение ответа от сервера
    data = client_socket.recv(1024)
    print(f"Received from server: {data.decode()}")

client_socket.close()
