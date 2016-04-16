import socket
import time
import sys,numpy,datetime
from matplotlib import pyplot
from interface import interface
from instrument import instrument
from prologix_ether_gpib import c_prologix_ether_gpib
from network_analyzer import c_network_analyzer

class c_hp8753c(c_network_analyzer):
	def __init__(self,_interface):
		c_network_analyzer.__init__(self,_interface)
	def plot(self,data,filename=None,mode=0):
		[x,d1,d2]=data
		if mode==0:
			pyplot.plot(x,d1)
		else:
			print 'mode not 0, not set yet'
		if filename:
			pyplot.savefig(filename)
		else:
			pyplot.show()
		return filename


	def read_screen_asis(self):
		self.write('++clr')
		self.write('STAR?')
		start=float(self.read())
		self.write('STOP?')
		stop=float(self.read())
		self.write('SPAN?')
		span=float(self.read())
		self.write('POIN?')
		point=int(float(self.read()))
		f_inc=span/(point-1);
		time.sleep(0.1)
		self.write('FORM4')
		self.write('OUTPFORM')
#self.ibloc()
		time.sleep(0.3)
		i=0;
		x=[]
		d1=[]
		d2=[]
		lentoread=50*point
		data=''
		index=0
		while len(data)<lentoread and index<10:
			index=index+1
			data=data+self.read(cnt=lentoread)
#	self.ibloc()
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
		return numpy.array([x,d1,d2]).transpose()

if __name__=="__main__":
	hp8753c_port=c_prologix_ether_gpib(gpib_addr=16)
	hp8753c=c_hp8753c(hp8753c_port)
	fig=pyplot.figure(1)
	pyplot.ion()
	while (1):
		[x,d1,d2]=hp8753c.read_screen_asis()
		fig.clear()
		pyplot.plot(x,d1)
		pyplot.draw()

#	pyplot.show()
	datetimestr=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	numpy.savetxt('./data_and_plots/hp8753c_%s.dat'%datetimestr,numpy.array([x,d1,d2]).transpose())
