### Remote control code (Client)

import socket
from inputs import get_key

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.2.64", 5432))
# s.send(b'Message from client to server.')

while True:
    events = get_key()
    for event in events:
        s.send(encode(event.ev_type), "utf-8")
s.close()