from time import sleep
from string import atoi

class instrument(object):
	def __init__(self,_interface):
		self.interface=_interface
	def read(self,cnt=1024,delay=1.0):
		return self.interface.read_interface(cnt=cnt,delay=delay)
	def write(self,cmd,delay=0):
		self.interface.write_interface(cmd=cmd,delay=delay)
	def reset(self):
	 	pass
	def local(self):
		self.inst.ibloc()
	def idn(self):
		self.write('*IDN?;')
#		sleep(0.5)
		return self.read()

if __name__ == "__main__":
	pass
