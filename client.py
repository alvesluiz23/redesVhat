import socket
import threading


host = ""
port = 8302

def receive_message(conn):
        while(True):
            data = conn.recv(1024)
            print(data.decode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host,port))
    thread_receive = threading.Thread(target=receive_message, args=(s,))
    thread_receive.start()
    while(True):
        a =input()
        s.send(a.encode())