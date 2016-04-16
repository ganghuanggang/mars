from interface import interface
from instrument import instrument
from prologix_ether_gpib import c_prologix_ether_gpib
from matplotlib import pyplot
#from gpib_inst import gpib_inst
import numpy as np
from string import atoi
import struct,time
class power_supply(instrument):
	def __init__(self,_interface):
		instrument.__init__(self,_interface)

if __name__=="__main__":
	keysight_e3633a_port=c_prologix_ether_gpib(gpib_addr=5)
	keysight_e3633a=power_supply(keysight_e3633a_port)
	print keysight_e3633a.idn()
	for i in range(1):
		keysight_e3633a.write('outp off')

		time.sleep(2)
		keysight_e3633a.write('curr:prot:stat: off')
		keysight_e3633a.write('outp on')
		time.sleep(0.5)
		keysight_e3633a.write('curr:prot:stat: on')
		time.sleep(2)

