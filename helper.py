# ALS*
import socket
import threading
import sys

sys.argv.append

PORT = 8910
HOST = socket.gethostbyname(socket.gethostname())
HEADER = 64
BUFF = 120
DISCONNECT_MESSAGE = "!DISCONNECT"
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
#sock.setblocking(False)
maxbytes = 10000

PORT = 8910
HEADER = 64
SIZE = 110
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname()) #"192.168.101.106" # comma 172.29.59.236
send_lenght = None

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((SERVER,PORT))


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        data = conn.recv(HEADER).decode("utf-8")
        if data:
            msg_length = int(data)
            if msg_length == BUFF:
                cstring = conn.recv(msg_length).decode("utf-8")
                print(f"[{addr}] | {cstring}")
            else:
                msg = conn.recv(msg_length).decode("utf-8")
                if msg == DISCONNECT_MESSAGE:
                    connected = False
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode("utf-8"))
    conn.close()


def start():
    sock.listen()
    print(f"[LISTENING] Server is listening on {HOST}")
    while True:
        conn, addr = sock.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
       

##########

def send(msg):
    message = msg.encode("utf-8")
    msg_length = len(message)
    send_lenght = str(msg_length).encode("utf-8")
    send_lenght += b" " * (HEADER - len(send_lenght))
    socket.send(send_lenght)
    socket.send(message)
    if send_lenght == SIZE:
        socket.recv(SIZE)
    else:
        print(socket.recv(HEADER).decode("utf-8"))

def main():
    socket.connect((SERVER,PORT))

if __name__ == "__main__":
    start()
    main()
