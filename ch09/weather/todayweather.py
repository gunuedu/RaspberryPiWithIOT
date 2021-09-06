#!/usr/bin/python3
import kma
import RPi.GPIO as GPIO
import time

redPin = 18
yellowPin = 23
greenPin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(yellowPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)

GPIO.output(redPin, False)
GPIO.output(yellowPin, False)
GPIO.output(greenPin, False)

lat = 37.43223
lon = 127.12905
mincount = 0
wcode = 0

while mincount < 60:
    data = kma.getWeather(lat, lon)
    for item in data:
        day = int(item[1])
        hour = int(item[0])
        if day == 0 and hour >= 12:
            wcode = kma.getWeatherCode(item[2])
            break
    if wcode >= 1 and wcode <= 2:
        GPIO.output(greenPin, True)
        print( "맑음, 구름 조금")
    elif wcode >= 3 and wcode <= 4:
        GPIO.output(yellowPin, True)
        print( "구름 많음, 흐림")
    elif wcode >= 5:
        GPIO.output(redPin, True)
        print( "비, 눈")
    mincount += 1
    time.sleep(60)

GPIO.output(redPin, False)
GPIO.output(yellowPin, False)
GPIO.output(greenPin, False)
