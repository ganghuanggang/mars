from spectrum_analyzer import spectrum_analyzer
import numpy
from string import atoi
import struct 

from prologix_ether_gpib import c_prologix_ether_gpib
from matplotlib import pyplot

class c_sa_fsp38(spectrum_analyzer):
	def __init__(self,_interface):
		spectrum_analyzer.__init__(self,_interface)

if __name__=="__main__":
	fsp38_port=c_prologix_ether_gpib(gpib_addr=20)
	fsp38=c_sa_fsp38(fsp38_port)
	print fsp38.idn()
	x=fsp38.read_x()
	y=fsp38.read_y()
	pyplot.plot(x,y)
	pyplot.grid()
	pyplot.show()
