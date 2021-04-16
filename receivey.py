# Raspberry Pi code (Server)

import socket
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.2.64", 5432))
s.listen(5)

while True:
    try:
        print("Searching for a connection...")
        clientsocket, address = s.accept()
        print(f"{address[0]}: ")
        clientsocket.send(bytes("Connected to the server successfully", "utf-8"))
    except:
        clientsocket.close()
        break

clientsocket.close()