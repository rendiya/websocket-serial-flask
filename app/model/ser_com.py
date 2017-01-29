#shell:startup

import serial
import time
#from app import config

ser = serial.Serial(port='/dev/ttyACM0',\
	baudrate=9600,\
	parity=serial.PARITY_NONE,\
	stopbits=serial.STOPBITS_ONE,\
	bytesize=serial.EIGHTBITS,\
	timeout=0)

print("connected to: " + ser.portstr)

#this will store the line
def main():
#while True:
	try:
		print "loopq"
		data = ser.read(99999)
		print data
		if data is "":
			print "data kosong"
		else:
			print "nyimpen db"
	except Exception:
		main()
	time.sleep(1)
	#ser.close()
	main()

if __name__ == "__main__":
	main()
