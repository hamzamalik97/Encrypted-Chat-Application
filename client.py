import socket
import threading
from crypto_utils import encrypt_message, decrypt_message

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

username = input("Enter your username: ")
client.send(username.encode())

def receive():
    while True:
        try:
            message = client.recv(1024).decode()

            # System messages (not encrypted)
            if "[" in message:
                print(f"\n{message}")
            else:
                decrypted = decrypt_message(message)
                print(f"\n{decrypted}")

        except:
            print("Disconnected from server")
            break

def write():
    while True:
        message = input()
        encrypted = encrypt_message(message)
        client.send(encrypted.encode())

threading.Thread(target=receive).start()
threading.Thread(target=write).start()