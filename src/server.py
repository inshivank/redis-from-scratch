import socket
import threading


HOST = "127.0.0.1"
PORT = 6379
BUFFER_SIZE = 1024


def handle_client(connection):
    try:
        while True:
            data = connection.recv(BUFFER_SIZE)
            if not data:
                break

            print(data)
    finally:
        connection.close()


def start():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print("Redis server started on port 6379")

        while True:
            connection, _ = server_socket.accept()
            print("Client connected")

            client_thread = threading.Thread(
                target=handle_client,
                args=(connection,),
                daemon=True,
            )
            client_thread.start()
