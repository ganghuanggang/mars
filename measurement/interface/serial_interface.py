from interface import interface
from serial import Serial
import time
class serial_interface(interface,Serial):
	def __init__(self,port=None, baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=False, rtscts=False, writeTimeout=None, dsrdtr=False, interCharTimeout=None):
		Serial.__init__(self,port=port,baudrate=baudrate,bytesize=bytesize,parity=parity,stopbits=stopbits,timeout=timeout,xonxoff=xonxoff,rtscts=rtscts,writeTimeout=writeTimeout,dsrdtr=dsrdtr,interCharTimeout=interCharTimeout)
		interface.__init__(self)
		self.flushOutput()
		self.flushInput()
		self.flush()
	def __del__(self):
		self.close()
	def write_interface(self,cmd,delay=0.0):
		res=Serial.write(self,data=cmd+'\n')
		time.sleep(delay)
		return res
	def read_interface(self,cnt=100,delay=0.0):
		time.sleep(delay)
		print 'read_interface'
		r1=Serial.readline(self)#,size=cnt)
		return r1

		
if __name__=="__main__":
	ser=serial_interface(0)
	ser.write('*idn?\n')
	print ser.read_interface()
#	print ser.readline()

