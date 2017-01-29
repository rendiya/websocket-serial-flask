import serial #for port opening
import sys #for exceptions
import time
#from app import config

class Serializer: 
    def __init__(self, port=None, baudrate=None, timeout=20,stopbits=None,bytesize=None,parity=None,waiting=False):

        if waiting is False:
            self.port = serial.Serial(port = port, baudrate=baudrate, 
            timeout=timeout, writeTimeout=timeout,stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE)
        else:
            self.port = serial.Serial(port = port, baudrate=baudrate, 
            timeout=timeout, writeTimeout=timeout,stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE)
            self.port.in_waiting

    def open(self): 
        ''' Open the serial port.'''
        self.port.open()

    def close(self): 
        ''' Close the serial port.'''
        self.port.close() 

    def send(self, msg):
        self.port.write(msg)

    def recv(self,numberline=None):
    	if numberline is None:
	        return self.port.readline()
        else:
	        return self.port.read(numberline)

#PORT = '/dev/ttyACM0' #Esto puede necesitar cambiarse

def main():
    test_port = Serializer(port = '/dev/ttyACM0',baudrate=9600)
    try:
        test_port.open()
    except Exception as e:
    	print e
    while True:
    	test_port.send(msg="abc")
        print(test_port.recv())
        time.sleep(1)
        test_port.send(msg="bca")
        print(test_port.recv())
