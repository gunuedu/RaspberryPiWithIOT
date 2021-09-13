import serial

con = serial.Serial('/dev/ttyS0', 9600, timeout=5)

while True:
    text = input("Input any text message: ")
    print( "Number of output characters : %d" % con.write(bytes(text.encode())) )

