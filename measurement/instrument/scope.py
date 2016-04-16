from matplotlib import pyplot
from serial_interface import serial_interface
from instrument import instrument
import struct,time
class scope(instrument):
	def __init__(self,_interface):
		instrument.__init__(self,_interface)
	def curve(self,channel=1):
		self.write('data:width 1\n')
		self.write('data:enc rib\n')
		self.write('data:source ch1\ncurve?\n')
		time.sleep(0.1)
		rd=self.read()
		data=self.decode_rib(rd)
		print 'rd',rd,rd.encode('hex'),len(rd),type(rd),'data',data
		return data
	def decode_rib(self,data):
		intd=[]
		if data[0]=='#':
			print 'decode'
			lenlen=int(data[1])
			length=int(data[2:2+lenlen])
			if len(data[2+lenlen:-1])==length:
				intd=struct.unpack('<'+str(length)+'b',data[2+lenlen:-1])
		else:
			print 'format not recorgnized'
		return intd
	def curves(self):
		self.write('data:width 1\n')
		self.write('data:enc rib\n')
		self.write('data:source ch1\ncurve?\ndata:source ch2\ncurve?\ndata:source ch3\ncurve?\ndata:source ch4\ncurve?\n')
		data1=self.decode_rib(self.read())
		data2=self.decode_rib(self.read())
		data3=self.decode_rib(self.read())
		data4=self.decode_rib(self.read())
		return [data1,data2,data3,data4]
	
if __name__=="__main__":
	scope_port=serial_interface(0)
	scope=scope(scope_port)
	scope.write('*rst?\n')
	print scope.idn()
	[data1,data2,data3,data4]=scope.curves()
	pyplot.plot(data1)
	pyplot.plot(data2)
	pyplot.plot(data3)
	pyplot.plot(data4)
	pyplot.show()
#	print scope.curve()
	'''
import time,struct
def decode_rib(data):
	intd=[]
	if data[0]=='#':
		lenlen=int(data[1])
		length=int(data[2:2+lenlen])
		if len(data[2+lenlen:-1])==length:
			intd=struct.unpack('<'+str(length)+'b',data[2+lenlen:-1])
	return intd
ser=serial.Serial(0)
ser.flushOutput()
print 'flush output'
ser.flushInput()
print 'flush input'
ser.flush()
ser.write('*rst?\n')
ser.write('*idn?\n')
idn=ser.readline()
print idn
ser.write('data:width 1\n')
ser.write('data:enc rib\n')
data=''
ser.write('select:ch1 on\n')
ser.write('select:ch2 on\n')
ser.write('select:ch3 on\n')
ser.write('select:ch4 on\n')
print len(data)
tstart=time.time()
ser.write('data:source ch1\ncurve?\ndata:source ch2\ncurve?\ndata:source ch3\ncurve?\ndata:source ch4\ncurve?\n')
data1=decode_rib(ser.readline())
#print len(data)
data2=decode_rib(ser.readline())
#print len(data)
data3=decode_rib(ser.readline())
#print len(data)
data4=decode_rib(ser.readline())
#print len(data)
#data=ser.read(ser.inWaiting())
#for src in ['ch1','ch2','ch3','ch4']:
#	ser.write('data:source '+src+'\n')
#	ser.write('data:source?\n')
#	print ser.readline()
#	ser.write('curve?\n')
#	data+=ser.readline()
print time.time()-tstart
print len(data1),len(data2),len(data3),len(data4)
print data1[0:20]
print data2[0:20]
print data3[0:20]
print data4[0:20]
pyplot.plot(data1)
pyplot.plot(data2)
pyplot.plot(data3)
pyplot.plot(data4)
pyplot.show()
ser.close()
from vxi11Device import Vxi11Device
import time
class vxi11(interface,Vxi11Device):
	def __init__(self,ip):
		interface.__init__(self)
		Vxi11Device.__init__(self,ip,"inst0")
	def __del__(self):
		print 'destroy 1'
		self.destroy()
		print 'destroy 2'
		#Vxi11Device.__del__(self)
	def write(self,cmd,delay=0.0):
		res=Vxi11Device.write(self,cmd=cmd+'\n')
		time.sleep(delay)
		return res
	def read(self,cnt=100,delay=1.0):
		time.sleep(delay)
		r1=Vxi11Device.read(self,requestSize=cnt)
		return r1

if __name__=="__main__":
	ipaddr="8c-8e-76-0-8c-db.dhcp.lbl.gov"
	bnc=vxi11(ipaddr)
	bnc.write("*IDN?\r\n")
	print bnc.read()

import socket
import time
import sys
from matplotlib import pyplot
from interface import interface
from instrument import instrument
from prologix_ether_gpib import prologix_ether_gpib

class network_analyzer(instrument):
	def __init__(self,_interface):
		instrument.__init__(self,_interface)
if __name__=="__main__":
	hp8753c_port=prologix_ether_gpib(gpib_addr=16)
	hp8753c=network_analyzer(hp8753c_port)
	print hp8753c.idn()
	'''
