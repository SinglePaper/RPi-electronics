import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
for x in range(0,3):
    GPIO.output(7,True)
    time.sleep(1)
    print("On")
    GPIO.output(7,False)
    time.sleep(1)
    print("Off")
print("Done")
GPIO.cleanup()