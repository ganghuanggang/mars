import socket
import time
import sys,numpy,datetime
from matplotlib import pyplot
from interface import interface
from instrument import instrument
from prologix_ether_gpib import c_prologix_ether_gpib

class c_network_analyzer(instrument):
	def __init__(self,_interface):
		instrument.__init__(self,_interface)
if __name__=="__main__":
	hp8753c_port=c_prologix_ether_gpib(gpib_addr=16)
	hp8753c=c_network_analyzer(hp8753c_port)
	hp8753c.write('++clr')
	hp8753c.write('STAR?')
	start=float(hp8753c.read())
	hp8753c.write('STOP?')
	stop=float(hp8753c.read())
	hp8753c.write('SPAN?')
	span=float(hp8753c.read())
	hp8753c.write('POIN?')
	point=int(float(hp8753c.read()))
	f_inc=span/(point-1);
	print point,start,stop,span
	time.sleep(1)
	hp8753c.write('FORM4')
	hp8753c.write('OUTPFORM')
#hp8753c.ibloc()
	time.sleep(3)
	i=0;
	x=[]
	d1=[]
	d2=[]
	lentoread=50*point
	data=''
	index=0
	while len(data)<lentoread and index<10:
		index=index+1
		data=data+hp8753c.read(cnt=lentoread)
	print data,len(data),len(data.split('\n')),index
#	hp8753c.ibloc()
	for d12 in data.split('\n'):
		if d12:
			df12=d12.split(',')
			d1i=float(df12[0]);
			d2i=float(df12[1]);
			xi=start+i*f_inc;
			i=i+1;
			d1.append(d1i);
			d2.append(d2i);
			x.append(xi);
	pyplot.plot(x,d1)
	pyplot.show()
	print point,start,stop,span,len(x)
