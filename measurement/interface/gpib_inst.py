from time import sleep
from Gpib import *
from string import atoi
import matplotlib.pyplot as plt
import numpy as np
import struct

class gpib_inst:
	def open(self):
		return Gpib(self.name)
	def read(self,length=1024):
		return self.inst.read(len=length)
	def write(self,cmd):
		self.inst.write(cmd)
	def inst_id(self):
		self.write('*IDN?')
		sleep(0.5)
		return self.read()
	def __init__(self,_name):
		self.name=_name
		self.inst=self.open()
	def reset(self):
	 	pass
	def local(self):
		self.inst.ibloc()

if __name__ == "__main__":
	a=gpib_inst('rs_fsp38')
	print a.inst_id()
