"""A command-line client for the beginner TCP chat project."""

import socket
import threading


HOST = "127.0.0.1"
PORT = 50000


def receive_messages(client_socket):
    """Print messages as they arrive, independently of keyboard input."""
    reader = client_socket.makefile("r", encoding="utf-8")
    try:
        for line in reader:
            print(line.rstrip())
    except OSError:
        pass
    finally:
        reader.close()
        print("Disconnected from the chat server.")


def main():
    username = input("Choose a chat name: ").strip()
    if not username:
        username = "Guest"

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        client_socket.sendall((username + "\n").encode("utf-8"))
    except ConnectionRefusedError:
        print("Could not connect. Start server.py first, then try again.")
        client_socket.close()
        return

    receiver = threading.Thread(
        target=receive_messages,
        args=(client_socket,),
        daemon=True,
    )
    receiver.start()

    print("Connected. Type a message and press Enter. Type /quit to leave.")
    try:
        while True:
            message = input()
            if message.strip().lower() == "/quit":
                break
            if message.strip():
                client_socket.sendall((message + "\n").encode("utf-8"))
    except (EOFError, KeyboardInterrupt, OSError):
        pass
    finally:
        try:
            client_socket.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        client_socket.close()
        print("You left the chat.")


if __name__ == "__main__":
    main()
