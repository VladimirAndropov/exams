import asyncio

async def tcp_client():
    reader, writer = await asyncio.open_connection('localhost', 8888)

    message = "Hello, server!"
    print(f'Send: {message}')
    writer.write(message.encode())

    data = await reader.read(1024)
    print(f'Received: {data.decode()}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_client())
