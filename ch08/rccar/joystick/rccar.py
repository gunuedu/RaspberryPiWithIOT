#!/usr/bin/python3
from flask import Flask, request, render_template
import cv2
import base64
import RPi.GPIO as gpio
import math

#Motor 1 GPIO Pins
DRIVE_DIR = 4 #IC3A
DRIVE_GO = 17 #IC3,4EN

#Motor 2 GPIO Pins
FRONT_DIR = 25 #IC1A
FRONT_GO = 10 #IC1,2EN

def command(speed, angle):
    if speed < 0.5:
        angle = math.pi / 2
    if angle > 0:
        gpio.output(DRIVE_DIR, gpio.HIGH)
    else:
        gpio.output(DRIVE_DIR, gpio.LOW)
    pwm2.ChangeDutyCycle(abs(speed)*10)
    dir = abs(angle) - math.pi / 2
    if dir > 0:
        gpio.output(FRONT_DIR, gpio.HIGH)
    else:
        gpio.output(FRONT_DIR, gpio.LOW)
    pwm1.ChangeDutyCycle(abs(dir)*200/math.pi)

gpio.setwarnings(False)
gpio.setmode( gpio.BCM )

#Pin Output Setup
gpio.setup(FRONT_GO, gpio.OUT)
gpio.setup(FRONT_DIR, gpio.OUT)
gpio.setup(DRIVE_GO, gpio.OUT)
gpio.setup(DRIVE_DIR, gpio.OUT)

#Pin Initialization
gpio.output(FRONT_GO, gpio.LOW)
gpio.output(FRONT_DIR, gpio.LOW)
gpio.output(DRIVE_GO, gpio.LOW)
gpio.output(DRIVE_DIR, gpio.LOW)

#Pin PWM
pwm1=gpio.PWM(FRONT_GO, 500)
pwm2=gpio.PWM(DRIVE_GO, 500)
pwm1.start(0)
pwm2.start(0)

cam=cv2.VideoCapture(0)
if cam.isOpened()==False:
    print("cant open cam")
    exit()
cam.set(cv2.CAP_PROP_FRAME_WIDTH,320)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,240)

app = Flask(__name__, template_folder=".")

#respone image for ajax by base64 string
@app.route('/getImage')
def get_image2base64():
    global cam
    ret,image=cam.read()
    gImage=cv2.flip(image,0)
    jpgImage=cv2.imencode(".jpeg",gImage)[1].tostring()
    encodedStr=base64.b64encode(jpgImage)
    return encodedStr

#control rccar
@app.route('/rccar', methods=['POST'])
def control_rccar():
    speed=float(request.form.get('speed'))
    angle=float(request.form.get('angle'))
    command(speed, angle)
    return ''

@app.route('/')
def do_route():
    return render_template("rccar.html")

@app.route('/joystick.js')
def do_joystick():
    return render_template("joystick.js")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
