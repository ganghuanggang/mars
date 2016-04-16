import socket
import time
import sys
from matplotlib import pyplot
from interface import interface
class c_prologix_ether_gpib(interface):
	def __init__(self,ip='0-21-69-1-1a-f7.dhcp.lbl.gov',gpib_addr=16,auto=0,tmo=500,eos=2,eoi=1,eot=0):
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
		self.auto=auto
		self.tmo=tmo
		self.eos=eos
		self.eoi=eoi
		self.eot=eot
		self.sock.settimeout(tmo/1000.0)
		self.sock.connect((ip,1234))
#		time.sleep(10)
		self.send("++mode 1\n")
		self.send("++auto %d\n"%self.auto)
		self.send("++read_tmo_ms %d\n"%self.tmo)
#		self.send("++eoi\n")
#		print 'eoi',self.recv(cnt=100,delay=0.1)
		#self.send("++eos\n")
		#time.sleep(0.1)
		#print 'eos',self.recv(100)
		self.send("++eos %d\n"%self.eos)
		self.send("++eoi %d\n"%self.eoi)
		self.send("++eot_enable %d\n"%self.eot)
		self.send("++addr %d\n"%gpib_addr)
#		self.send("++clr\n")
#		self.write_interface("*idn?\n")
#		print self.read_interface(delay=1)
	def ver(self):
		self.send("++ver\n")
		return self.recv(100,delay=0.1)
	def send(self,cmd):
		return self.sock.send(cmd)
	def recv(self,cnt,delay=0.1):
		time.sleep(delay)
		return self.sock.recv(cnt)
	def write_interface(self,cmd,delay=0.0):
		res=self.sock.send(cmd+'\n')
		time.sleep(delay)
		return res
	def read_interface(self,cnt=100,delay=0.0):
		time.sleep(delay)
		if not self.auto:
			self.send("++read\n")
		#time.sleep(delay)
		r1=self.recv(cnt=cnt,delay=delay)
		#print self.send("++read\n")
		#r2=self.recv(cnt=cnt,delay=delay)
		return r1#+r2
	def close(self):
		if self.sock:
			self.sock.close()
	def __del__(self):
		self.close()
#print '2',sock.send("*idn? "+u"\x1b\n\x1b\x10"+"\n")
#print '2',sock.send("*idn? "+u"\x1b\n"+"\n")
if __name__=="__main__":
	hp8753c=c_prologix_ether_gpib(gpib_addr=16)
#	hp8753c.write('star?')
#	print hp8753c.read(delay=1)
#	hp8753c.write('stop?')
#	print hp8753c.read(delay=2)
	#hp8753c.write('span?')
	#print hp8753c.read(delay=2)
	#hp8753c.write('poin?')
	#print hp8753c.read(delay=2)
#	hp8753c.write('*rst')
#	time.sleep(25)
#	try:
#		print hp8753c.read(cnt=100,delay=2.0)
#	except:
#		pass
#	hp8753c.write(sys.argv[1])
#	idn=hp8753c.read(cnt=100,delay=2.0)
#	print idn
#	print idn.encode('hex')
#	time.sleep(2.0)
#	hp8753c.write('POIN?')
#	read1=hp8753c.read(delay=3.0)
#	print read1
#	point=int(float(
	if (1):
		point=201
		start=0.3e6
		stop=300e6
		span=stop-start;
		f_inc=span/(point-1);
		hp8753c.write_interface('form4')
		hp8753c.write_interface('outpform')
		data=hp8753c.read_interface(cnt=50*point,delay=5)
		print data
		i=0
		x=[]
		d1=[]
		d2=[]
		for d12 in data.split('\n'):
			if len(d12)>0:
				df12=d12.split(',')
				d1i=float(df12[0]);
				d2i=float(df12[1]);
				xi=start+i*f_inc;
				i=i+1;
				d1.append(d1i);
				d2.append(d2i);
				x.append(xi);
		pyplot.plot(x,d1)
		pyplot.show()
	hp8753c.close()
#	hp8753.send("++read \n")
#	time.sleep(1)
#	print sock.recv(100)
