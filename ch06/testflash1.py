import spidev, time

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000
#spi.mode - 3

def hex_print(the_list):
    i = 0
    string = '['
    for i in range(0, len(the_list)):
       if i == (len(the_list)-1):
          string = string + hex(the_list[i])
       else:
           string = string + hex(the_list[i]) + ', '
    string = string + ']'
    return string

def ee_write_buffer(offset, value):
    #spi.xfer2([0x84, 0xff, offset>>8, offset&0xff, value],3000000,12)
    spi.xfer2([0x84, 0xff, offset>>8, offset&0xff, value])

def ee_read_buffer(offset):
    #value = spi.xfer2([0xd4, 0xff, offset>>8, offset&0xff, 0xff, 0xff],3000000,12)
    value = spi.xfer2([0xd4, 0xff, offset>>8, offset&0xff, 0xff, 0xff])[5]
    return value

def ee_read_id():
    value = spi.xfer2([0x9f, 0xff, 0xff, 0xff, 0xff, 0xff])
    print( "Device ID : " + hex_print(value[1:]))
    return value[1:]

def ee_read_status():
    value = spi.xfer2([0xD7, 0xff])
    print( "Device Status : " + hex_print(value[1:]))
    return value[1]

ee_read_status()
ee_read_id()

for i in range(5):
    print(ee_read_buffer(i))
    time.sleep(0.005)

for i in range(5):
    ee_write_buffer(i, i+1)
if False: #ee_read_buffer(1) != 1:
    print( "open error")
else:
    for i in range(5):
        print( ee_read_buffer(i))
        time.sleep(0.005)

spi.close()
