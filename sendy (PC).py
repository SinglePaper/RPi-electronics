import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect('192.168.2.64', 8080)
sock.send("This is a test.")
sock.recv(4096)
sock.close()