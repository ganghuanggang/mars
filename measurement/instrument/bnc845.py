from signal_generator import signal_generator
from vxi11 import c_vxi11
class c_sg_bnc845(signal_generator):
	def __init__(self,_interface):
		signal_generator.__init__(self,_interface)
	def set_freq(self,freq,unit='Hz'):
		self.write("FREQ %s %s\r\n"%(str(freq),unit))
	def set_power(self,power,unit='dBm'):
		self.write("POW %s %s\r\n"%(str(power),unit))
	def output(self,on=0):
		self.write("OUTP %s \r\n"%('ON' if on else 'OFF'))


if __name__=="__main__":
	bnc845_port=c_vxi11("8c-8e-76-0-8c-db.dhcp.lbl.gov")
	bnc845=c_sg_bnc845(bnc845_port)
	print bnc845.idn()
	bnc845.write("SOUR:ROSC:OUTP:STAT ON \r\n")
	bnc845.write("SOUR:ROSC:OUTP:FREQ 10 MHz \r\n")
	bnc845.write("SOUR:ROSC:OUTP:STAT?  \r\n")
	print bnc845.read()
	bnc845.set_freq(20e6)
	print 'done'

