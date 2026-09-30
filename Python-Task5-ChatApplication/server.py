"""A small threaded TCP chat server for the beginner project."""

from datetime import datetime
import socket
import threading


HOST = "127.0.0.1"  # localhost: accessible only from this computer
PORT = 50000

clients = {}  # socket -> (username, per-client send lock)
clients_lock = threading.Lock()


def timestamp():
    return datetime.now().strftime("%H:%M")


def broadcast(message):
    """Send one line to every connected client, including the sender."""
    data = (message + "\n").encode("utf-8")
    with clients_lock:
        recipients = list(clients.items())

    for client_socket, (_username, send_lock) in recipients:
        try:
            with send_lock:
                client_socket.sendall(data)
        except OSError:
            # The handler for this client will remove it from the client list.
            pass


def handle_client(client_socket, address):
    """Read messages from one client until it disconnects."""
    username = "Guest"
    joined = False
    reader = client_socket.makefile("r", encoding="utf-8")

    try:
        username = reader.readline().strip() or "Guest"
        send_lock = threading.Lock()
        with clients_lock:
            clients[client_socket] = (username, send_lock)
        joined = True

        print(f"{username} connected from {address}.")
        broadcast(f"[{timestamp()}] {username} joined the chat.")

        for line in reader:
            message = line.strip()
            if message:
                broadcast(f"[{timestamp()}] {username}: {message}")
    except (ConnectionError, OSError):
        pass
    finally:
        if joined:
            with clients_lock:
                clients.pop(client_socket, None)
            broadcast(f"[{timestamp()}] {username} left the chat.")

        try:
            reader.close()
        except OSError:
            pass
        client_socket.close()
        print(f"{username} disconnected.")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Chat server listening on {HOST}:{PORT}. Press Ctrl+C to stop.")

        try:
            while True:
                client_socket, address = server_socket.accept()
                worker = threading.Thread(
                    target=handle_client,
                    args=(client_socket, address),
                    daemon=True,
                )
                worker.start()
        except KeyboardInterrupt:
            print("\nServer stopping.")


if __name__ == "__main__":
    main()
