from signal_generator import signal_generator
from vxi11 import c_vxi11
class c_sg_agilent_33622a(signal_generator):
	def __init__(self,_interface):
		signal_generator.__init__(self,_interface)
	def set_freq(self,freq):#,unit='Hz'):
		#		self.write("FREQ:unit %s"%(unit))
		self.write("FREQ %s"%(str(freq)))
	def set_power(self,power,unit):
		self.write("volt:unit %s"%(unit))
		self.write("volt %s"%(str(power)))
	def output(self,on=0):
		self.write("OUTP %s "%('ON' if on else 'OFF'))


if __name__=="__main__":
	#	agilent_33622a_port=c_vxi11("A-33600-00000.dhcp.lbl.gov","inst0")
	agilent_33622a_port=c_vxi11('131.243.171.39','inst0')
	agilent_33622a=c_sg_agilent_33622a(agilent_33622a_port)
	print agilent_33622a_port.write("*idn?")
	print agilent_33622a_port.read()
	print agilent_33622a_port.write("*rst")
#	print agilent_33622a.idn()
#	agilent_33622a.set_freq(20.01e6,'Hz')
	agilent_33622a.set_power(-0.01,'dbm')
#	print 'done'

