from spectrum_analyzer import spectrum_analyzer
import numpy,time
from string import atoi
import struct 
import re

from prologix_ether_gpib import c_prologix_ether_gpib
from matplotlib import pyplot

class c_hp8563e(spectrum_analyzer):
	def __init__(self,_interface):
		spectrum_analyzer.__init__(self,_interface)
	def idn(self):
		self.write('id?;rev?;')
#       time.sleep(0.5)
		return self.read()

if __name__=="__main__":
	hp8563e_port=c_prologix_ether_gpib(gpib_addr=20,eos=0,eoi=0,tmo=500000)
	print hp8563e_port.ver()
#	pyplot.ion()
#	fig1=pyplot.figure()
	hp8563e=c_hp8563e(hp8563e_port)
#	hp8563e.write('++clr')
	if 0:
		hp8563e.write('ip;sngls;\n')
		hp8563e.write('cf 145MHz;sp 10MHz;\n')
		hp8563e.write('cf?;rb?\n')
		print hp8563e.read()
#		print hp8563e.idn()
#		hp8563e.write('FA200MHZ');
#		hp8563e.write('FB300MHZ');
	if(0):
		hp8563e.write('ts;done?;\n')
		time.sleep(0.1);
		hp8563e.write('TRA?');
		time.sleep(0.1);
#		print hp8563e.read()
		datas=hp8563e.read(65535);
		print len(datas)
		#hp8563e.ibloc();
#		print datas
		try:
			data=[float(d) for d in datas.split(',')];
#		fig=pyplot.figure()
			fig1.clear()
			pyplot.grid()
			pyplot.plot(data);
			pyplot.draw();


		except:
			pass
	while (1):
		hp8563e.write('mkpk hi;mka?;')
		s_amp=hp8563e.read()
		print s_amp
		m_amp=re.match('\s*(\S+)\s+(\S+)\s*',s_amp)
		if m_amp:
			amp=m_amp.group(2)
			print 'amp is:',amp, 
		hp8563e.write('mkf?;')
		s_freq=hp8563e.read()
		m_freq=re.match('\s*(\S+)\s*',s_freq)
#   print m_freq.groups()
		if m_freq:
			freq=m_freq.group(1)
			print 'freq is: ',freq

			#print hp8563e.idn()
			#x=hp8563e.read_x()
			#y=hp8563e.read_y()
		#pyplot.plot(x,y)
		#pyplot.grid()
		#pyplot.show()
