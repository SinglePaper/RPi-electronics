import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
for x in range(0,3):
    GPIO.output(7,True)
    time.sleep(.5)
    GPIO.output(7,False)
    GPIO.output(11,True)
    time.sleep(.5)
    GPIO.output(11,False)
print("Done")
GPIO.cleanup()