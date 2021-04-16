import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.2.64", 1234))
s.listen(5)

while True:
    print("Searching for a connection...")
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Connected to the server successfully", "utf-8"))
