# Remote control code (Client)

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.2.64", 5432))

while True:
    s.sendall(b'Received message from client.')
    msg = s.recv(1024)
    if msg == "":
        break
    print(msg.decode("utf-8"))
s.close()