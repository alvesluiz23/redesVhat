import socket
import threading




HOST = ""
port = 8302

def receive_message(conn):
        while(True):
            data = conn.recv(1024)
            print(data.decode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, port))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
       print("COnnectd by", addr)
       thread_receive = threading.Thread(target=receive_message, args=(conn,))
       thread_receive.start()
       while(True):
            a =input()
            conn.send(a.encode())
          