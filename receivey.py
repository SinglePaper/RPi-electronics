### Raspberry Pi code (Server)

import socket
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)  # Left motor forward
GPIO.setup(11,GPIO.OUT)  # Left motor backward
GPIO.setup(13,GPIO.OUT)  # Right motor forward
GPIO.setup(15,GPIO.OUT)  # Right motor backward

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.2.64", 5432))
s.listen(5)

while True:
    try:
        print("Searching for a connection...")
        clientsocket, address = s.accept()
        print(f"Successful connection with address {address[0]}.")
        while True:
            data = clientsocket.recv(1).decode("utf-8")
            if not data:
                break
            print(f"{address[0]}: " + data.decode("utf-8"))
            if clientsocket.recv(1) == "n":
                GPIO.output(7, False)
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(15, False)
            elif clientsocket.recv(1) == "f":
                GPIO.output(7, True)
                GPIO.output(11, False)
                GPIO.output(13, True)
                GPIO.output(15, False)
            elif clientsocket.recv(1) == "b":
                GPIO.output(7, False)
                GPIO.output(11, True)
                GPIO.output(13, False)
                GPIO.output(15, True)
            elif clientsocket.recv(1) == "l":
                GPIO.output(7, False)
                GPIO.output(11, False)
                GPIO.output(13, True)
                GPIO.output(15, False)
            elif clientsocket.recv(1) == "r":
                GPIO.output(7, True)
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(15, False)
        else:
            continue
    except:
        GPIO.cleanup()
        s.close()
        if 'clientsocket' in locals():
            clientsocket.close()
        break