import asyncio

async def handle_client(reader, writer):
    data = await reader.read(1024)
    message = data.decode()
    print(f"Received: {message}")

    print("Send: %s" % message)
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, 'localhost', 8888)
    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")

    async with server:
        await server.serve_forever()

asyncio.run(main())
