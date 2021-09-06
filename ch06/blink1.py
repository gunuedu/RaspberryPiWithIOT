import pigpio
import time
pi = pigpio.pi()
pi.set_mode(18, pigpio.OUTPUT)
while (True):
    pi.write(18, 1)
    time.sleep(1)
    pi.write(18, 0)
    time.sleep(1)
