from interface import interface
from instrument import instrument
from prologix_ether_gpib import c_prologix_ether_gpib
from matplotlib import pyplot
#from gpib_inst import gpib_inst
import numpy as np
from string import atoi
import struct 
class spectrum_analyzer(instrument):
	def __init__(self,_interface):
		instrument.__init__(self,_interface)

	def center_freq(self,freq_MHz):
		pass
	def span(self,span_MHz):
		pass
	def rbf(self,rbf_MHz):
		pass
	def read_x(self):
		self.write('FREQ:START?')
		start=float(self.read())
		self.write('FREQ:STOP?')
		stop=float(self.read())
		self.write('SWE:POIN?') 
		npoint=float(self.read())
		freq_point_1=np.arange(start,stop,(stop-start)/(npoint-1))
		freq_point=np.append(freq_point_1,stop)
		return freq_point
	def read_y(self):
		self.write('*cls')
		self.write('form real')
		self.write('trac? trace1')
		head=self.read(2)
		num=atoi(self.read(cnt=atoi(head[1])))
		data=self.read(cnt=num)
		u_format='=%df'%(num/4)
		datafmt=np.array(struct.unpack(u_format,data))
		tail=self.read(1)
		return datafmt

if __name__=="__main__":
	fsp38_port=c_prologix_ether_gpib(gpib_addr=20)
	fsp38=spectrum_analyzer(fsp38_port)
	print fsp38.idn()
	x=fsp38.read_x()
	y=fsp38.read_y()
	pyplot.plot(x,y)
	pyplot.grid()
	pyplot.show()
