import smbus
import os, sys
from datetime import *

os.system("echo 0x51 > /sys/class/i2c-adapter/i2c-1/delete_device")

I2C_ADDRESS = 0x51
bus = smbus.SMBus(1)  # if rev 1, use SMBus(0)

dt = datetime.now(timezone.utc)
tm = dt.timetuple()
print("system time(utc) : %s" % dt)

def dec_to_bcd(data):
    retvalue=[]
    for i in range(len(data)):
        retvalue.append((int(data[i]/10)*16) + (data[i]% 10))
    return retvalue

wday = tm.tm_wday + 1 #system Monday == 0, RTC Sunday == 0
if wday == 7: #system is Sunday
    wday = 0 # RTC vlaue set 0(Sunday)

data = dec_to_bcd([tm.tm_sec, tm.tm_min, tm.tm_hour, tm.tm_mday,
                    wday, tm.tm_mon, (tm.tm_year % 100)])
bus.write_i2c_block_data(I2C_ADDRESS, 0x02, data)

rdata = bus.read_i2c_block_data(I2C_ADDRESS, 0x02)
print("RTC Read (utc) : 20%x-%x-%x %x:%x:%x"
    % (rdata[6], rdata[5], rdata[3], rdata[2], rdata[1], rdata[0]) )

os.system("echo pcf8563 0x51 > /sys/class/i2c-adapter/i2c-1/new_device")
os.system("hwclock -r")
os.system("echo 0x51 > /sys/class/i2c-adapter/i2c-1/delete_device")
