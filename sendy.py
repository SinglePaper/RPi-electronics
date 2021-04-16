# Remote control code (Client)

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.2.64", 5432))

while True:
    s.sendall('Received message from client.')
    msg = s.recv(1024)
    if msg == "":
        print("Server Closed.")
        break
    print(msg.decode("utf-8"))
s.close()