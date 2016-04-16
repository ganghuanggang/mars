import socket
import time
import sys
from interface import interface
from instrument import instrument
from vxi11 import c_vxi11

class signal_generator(instrument):
	def __init__(self,_interface):
		instrument.__init__(self,_interface)
if __name__=="__main__":
	#	bnc845_port=c_vxi11("8c-8e-76-0-8c-db.dhcp.lbl.gov")
	#bnc845=signal_generator(bnc845_port)
	#print bnc845.idn()
	awg=c_vxi11("A-33600-00000.dhcp.lbl.gov","inst0")
	awg.write("*idn?\n")
	print awg.read()

