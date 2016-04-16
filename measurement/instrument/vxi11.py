from vxi11Device import Vxi11Device
import vxi11Device
from interface import interface
import time
class c_vxi11(interface,Vxi11Device):
	def __init__(self,host,device="inst0",proto='tcp'):
		interface.__init__(self)
		print host,device,proto
		Vxi11Device.__init__(self,host=host,device=device)
	def __del__(self):
		print 'destroy 1'
		self.destroy()
		print 'destroy 2'
		#Vxi11Device.__del__(self)
	def write_interface(self,cmd,delay=0.0):
		res=Vxi11Device.write(self,cmd=cmd+'\n')
		time.sleep(delay)
		return res
	def read_interface(self,cnt=100,delay=1.0):
		time.sleep(delay)
		r1=Vxi11Device.read(self,requestSize=cnt)
		return r1

if __name__=="__main__":
	#	ipaddr="8c-8e-76-0-8c-db.dhcp.lbl.gov"
	#bnc=c_vxi11(ipaddr)
	#bnc.write_interface("*IDN?\r\n")
	#print bnc.read_interface()
	ipaddr="A-33600-00000.dhcp.lbl.gov"
#	awg=c_vxi11Device.Vxi11Device("A-33600-00000.dhcp.lbl.gov","inst0")
#	Vxi11Device(ipaddr,"inst0")
	awg=c_vxi11(ipaddr)
	awg.write("*idn?\n")
	awg.read()


