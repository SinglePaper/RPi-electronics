import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.2.18", 5432))
s.listen(5)

while True:
    try:
        print("Searching for a connection...")
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established!")
        clientsocket.send(bytes("Connected to the server successfully", "utf-8"))
    except:
        clientsocket.close()
