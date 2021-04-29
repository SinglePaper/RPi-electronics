### Raspberry Pi code (Server)


## Using Wifi connection
# import socket
# import RPi.GPIO as GPIO
# import time

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(7,GPIO.OUT)  # Left motor forward
# GPIO.setup(11,GPIO.OUT)  # Left motor backward
# GPIO.setup(13,GPIO.OUT)  # Right motor forward
# GPIO.setup(15,GPIO.OUT)  # Right motor backward


# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(("192.168.2.64", 5432))
# s.listen(5)

# while True:
#     try:
#         print("Searching for a connection...")
#         clientsocket, address = s.accept()
#         print(f"Successful connection with address {address[0]}.")
#         while True:
#             data = clientsocket.recv(1).decode("utf-8")
#             if not data:
#                 break
#             print(f"{address[0]}: " + data)
#             if data == "f":
#                 GPIO.output(7, False)
#                 GPIO.output(11, True)
#                 GPIO.output(13, False)
#                 GPIO.output(15, True)
#             elif data == "b":
#                 GPIO.output(7, True)
#                 GPIO.output(11, False)
#                 GPIO.output(13, True)
#                 GPIO.output(15, False)
#             elif data == "l":
#                 GPIO.output(7, False)
#                 GPIO.output(11, False)
#                 GPIO.output(13, False)
#                 GPIO.output(15, True)
#             elif data == "r":
#                 GPIO.output(7, False)
#                 GPIO.output(11, True)
#                 GPIO.output(13, False)
#                 GPIO.output(15, False)
#             else:
#                 GPIO.output(7, False)
#                 GPIO.output(11, False)
#                 GPIO.output(13, False)
#                 GPIO.output(15, False)
#         else:
#             continue
#     except:
#         GPIO.cleanup()
#         s.close()
#         if 'clientsocket' in locals():
#             clientsocket.close()
#         break



## Using JS Website connection
from flask import Flask, jsonify, request, render_template
import random, json
import logging
from os import system

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.disabled = True

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)  # Left motor forward
GPIO.setup(11,GPIO.OUT)  # Left motor backward
GPIO.setup(13,GPIO.OUT)  # Right motor forward
GPIO.setup(15,GPIO.OUT)  # Right motor backward

direction = 0  # Forward
speed = 0

## Directions
# 0 - Forward
# 1 - Left
# 2 - Backward
# 3 - Right
#
# Layout:
#    0
#  1 2 3
##


@app.route('/receiver', methods = ['POST'])
def receiver():
    # read json + reply
    data = request.get_json(force=True)  # Get the json and turn it into a normal dict, ignore any mistakes that i made using force=True :wink:
    # Extract the data from data into global variables to use to control the motor
    direction = data['direction']
    speed = data['speed']

    if direction == 0:  # Forward
        GPIO.output(7, False)
        GPIO.output(11, True)
        GPIO.output(13, False)
        GPIO.output(15, True)
    elif direction == 1:  # Left
        GPIO.output(7, False)
        GPIO.output(11, True)
        GPIO.output(13, False)
        GPIO.output(15, False)
    elif direction == 2:  # Backward
        GPIO.output(7, True)
        GPIO.output(11, False)
        GPIO.output(13, True)
        GPIO.output(15, False)
    elif direction == 3:  # Right
        GPIO.output(7, False)
        GPIO.output(11, False)
        GPIO.output(13, False)
        GPIO.output(15, True)
    else:                 # Shouldn't happen but just in case: just shut off
        GPIO.output(7, False)
        GPIO.output(11, False)
        GPIO.output(13, False)
        GPIO.output(15, False)

    if speed == 0:        # Can't happen yet, but just to make sure I remember what to do with this variable. Speed 0 = still, Speed 1 = normal, Speed 2 = fast
        GPIO.output(7, False)
        GPIO.output(11, False)
        GPIO.output(13, False)
        GPIO.output(15, False)
    
    # Speed can be implemented by repeatedly turning the motors on and off on given intervals, but can't be bothered to do that right now.

    # Print out some debugging tools and make it look pretty :)
    system('clear')
    print("\n=======Controls=======")
    print("Direction: ", direction)
    print("Speed: ", speed)
    #       direction = data['direction']
    return 'OK'
@app.route('/')
def home_page():
    return render_template('index.html')

app.run(host='0.0.0.0', debug=True)
GPIO.cleanup()