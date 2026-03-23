import socket
import threading
from crypto_utils import decrypt_message
from datetime import datetime

HOST = '127.0.0.1'
PORT = 12345

clients = []
usernames = {}

def log_message(message):
    with open("chat.log", "a") as f:
        f.write(message + "\n")

def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                client.close()
                clients.remove(client)

def handle_client(conn, addr):
    try:
        username = conn.recv(1024).decode()
        usernames[conn] = username

        join_msg = f"[{username}] joined the chat"
        print(join_msg)
        log_message(join_msg)
        broadcast(join_msg)

        while True:
            msg = conn.recv(1024).decode()
            if not msg:
                break

            decrypted = decrypt_message(msg)
            full_msg = f"{username}: {decrypted}"

            print(full_msg)
            log_message(full_msg)

            broadcast(msg, conn)

    except:
        pass

    finally:
        username = usernames.get(conn, "Unknown")
        leave_msg = f"[{username}] left the chat"

        print(leave_msg)
        log_message(leave_msg)
        broadcast(leave_msg)

        clients.remove(conn)
        conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[STARTED] Server running on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        clients.append(conn)

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

start_server()