from gpib_inst import gpib_inst
import numpy as np
from string import atoi
import struct 

class src_agilent_e4425b(gpib_inst):
	def __init__(self):
		gpib_inst.__init__(self,'agi_e4425b')
	def power_off(self):
		self.write(':OUTPUT OFF')
	def power_on(self):
		self.write(':OUTPUT ON')
	def set_power(self,power_dbm):
		self.write(':POW %.2fdBm'%power_dbm)
	def get_power(self):
	 	self.write(':POW?')
		return self.read()
	def get_freq(self):
	 	self.write(':FREQ?')
		return self.read()
	def reset(self):
		self.write('*RST')
	def set_freq(self,freq_MHz):
		self.write(':FREQ:FIX %fMHz'%freq_MHz)
if __name__ == "__main__":
	a=src_agilent_e4425b()
	print a.inst_id()
	a.reset()
	a.power_off()
	a.set_freq(351.936)
	a.set_power(0)
	a.power_on()
	a.local()



