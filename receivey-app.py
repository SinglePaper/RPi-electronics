import socket
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)  # Left motor forward
GPIO.setup(11,GPIO.OUT)  # Left motor backward
GPIO.setup(13,GPIO.OUT)  # Right motor forward
GPIO.setup(15,GPIO.OUT)  # Right motor backward
GPIO.output(7, False)
GPIO.output(11, False)
GPIO.output(13, False)
GPIO.output(15, False)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 5432))
s.listen(3)

while True:
    try:
        print("Searching for a connection...")
        clientsocket, address = s.accept()
        print(f"Successful connection with address {address[0]}.")
        while True:
            try:
                data = clientsocket.recv(3).decode("utf-8")
                if not data:
                    break
                print(f"{address[0]}: " + data[0])
                if data[0] == "0":  # Forward
                    GPIO.output(7, True)
                    GPIO.output(11, False)
                    GPIO.output(13, False)
                    GPIO.output(15, True)
                elif data[0] == "1":  # Left
                    GPIO.output(7, True)
                    GPIO.output(11, False)
                    GPIO.output(13, True)
                    GPIO.output(15, False)
                elif data[0] == "2":  # Backward
                    GPIO.output(7, False)
                    GPIO.output(11, True)
                    GPIO.output(13, True)
                    GPIO.output(15, False)
                elif data[0] == "3":  # Right
                    GPIO.output(7, False)
                    GPIO.output(11, True)
                    GPIO.output(13, False)
                    GPIO.output(15, True)
                else:  # Shouldn't happen but just in case: just shut off
                    GPIO.output(7, False)
                    GPIO.output(11, False)
                    GPIO.output(13, False)
                    GPIO.output(15, False)

                if data[1] == "0":  # Can't happen yet, but just to make sure I remember what to do with this variable. Speed 0 = still, Speed 1 = normal, Speed 2 = fast
                    GPIO.output(7, False)
                    GPIO.output(11, False)
                    GPIO.output(13, False)
                    GPIO.output(15, False)
            except:
                continue
        else:
            continue
    except:
        GPIO.cleanup()
        s.close()
        if 'clientsocket' in locals():
            clientsocket.close()
        break