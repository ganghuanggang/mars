from gpib_inst import gpib_inst
import numpy as np
from string import atoi
import struct 
class LLRF4(gpib_inst):
	def __init__(self,a):
		gpib_inst.__init__(self,'rs_fsp38')
		print "init LLRF a=%s"%(a)

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
		num=atoi(self.read(length=atoi(head[1])))
		data=self.read(length=num)
		u_format='=%df'%(num/4)
		datafmt=np.array(struct.unpack(u_format,data))
		tail=self.read(1)
		return datafmt

if __name__ == "__main__":
	a=sa_fsp38()
	print a.inst_id()
	a.read_y()
	a.local()
