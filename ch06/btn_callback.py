import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN)
try:
    GPIO.wait_for_edge(24, GPIO.FALLING)
    print("Falling edge detected.")
except KeyboardInterrupt:
    GPIO.cleanup()     # clean up GPIO on CTRL_C
GPIO.cleanup()
