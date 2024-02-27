#>>> import serial
#>>> ser = serial.Serial('/dev/ttyUSB0')  # open serial port
#>>> print(ser.name)         # check which port was really used
#>>> ser.write(b'hello')     # write a string
#>>> ser.close()             # close port

import serial
import io
ser = serial.serial_for_url('tcp://', timeout=1)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

sio.write(unicode("hello\n"))
sio.flush() # it is buffering. required to get the data out *now*
hello = sio.readline()
print(hello == unicode("hello\n"))
