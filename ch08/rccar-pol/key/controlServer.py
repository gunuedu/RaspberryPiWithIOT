import RPi.GPIO as gpio

#Motor 1 GPIO Pins
LEFT_GO = 17 #IC1A
LEFT_DIR = 18 #IC1,2EN
#Motor 2 GPIO Pins
RIGHT_GO = 10 #IC3,4EN
RIGHT_DIR = 25 #IC3A

def forward():
    gpio.setmode(gpio.BCM)
    gpio.output(LEFT_GO, gpio.HIGH)
    gpio.output(LEFT_DIR, gpio.LOW)
    gpio.output(RIGHT_GO, gpio.HIGH)
    gpio.output(RIGHT_DIR, gpio.LOW)

def backward():
    gpio.setmode(gpio.BCM)
    gpio.output(LEFT_GO, gpio.HIGH)
    gpio.output(LEFT_DIR, gpio.HIGH)
    gpio.output(RIGHT_GO, gpio.HIGH)
    gpio.output(RIGHT_DIR, gpio.HIGH)

def left():
    gpio.setmode(gpio.BCM)
    gpio.output(LEFT_GO, gpio.HIGH)
    gpio.output(LEFT_DIR, gpio.LOW)
    gpio.output(RIGHT_GO, gpio.HIGH)
    gpio.output(RIGHT_DIR, gpio.HIGH)

def right():
    gpio.setmode(gpio.BCM)
    gpio.output(LEFT_GO, gpio.HIGH)
    gpio.output(LEFT_DIR, gpio.HIGH)
    gpio.output(RIGHT_GO, gpio.HIGH)
    gpio.output(RIGHT_DIR, gpio.LOW)

def stop():
    gpio.setmode(gpio.BCM)
    gpio.output(LEFT_GO, gpio.LOW)
    gpio.output(LEFT_DIR, gpio.LOW)
    gpio.output(RIGHT_GO, gpio.LOW)
    gpio.output(RIGHT_DIR, gpio.LOW)

def initMotors():
    gpio.setwarnings(False)
    gpio.setmode( gpio.BCM )

    #Pin Output Setup
    gpio.setup(LEFT_GO, gpio.OUT)
    gpio.setup(LEFT_DIR, gpio.OUT)
    gpio.setup(RIGHT_GO, gpio.OUT)
    gpio.setup(RIGHT_DIR, gpio.OUT)

    #Pin Initialization
    gpio.output(LEFT_GO, gpio.LOW)
    gpio.output(LEFT_DIR, gpio.LOW)
    gpio.output(RIGHT_GO, gpio.LOW)
    gpio.output(RIGHT_DIR, gpio.LOW)
