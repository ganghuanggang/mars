# https://holometer.fnal.gov/GH_FFT.pdf
import numpy,scipy
import scipy.signal
from matplotlib import pyplot

def test_signal(N=1000000.0,fs=10000.0,f1=1234.0,amp1=2.82842712474619,f2=2500.2157,amp2=1.0,ulsb=1e-3):
	TWOPI=6.28318530717959
	t=1.0*numpy.arange(N)/fs;
	u=amp1*numpy.sin(TWOPI*f1*t)+amp2*numpy.sin(TWOPI*f2*t)
	ur=numpy.floor(u/ulsb+0.5)*ulsb
	return [t,ur,fs,N]
def hft116d(N):
	z=2.0*numpy.pi*numpy.arange(N)/N
	wj=1-1.9575375*numpy.cos(z)+1.4780705*numpy.cos(2*z)-0.6367431*numpy.cos(3*z)+0.1228389*numpy.cos(4*z)-0.0066288*numpy.cos(5*z)
	return wj


def ps_psd(y,fs,window='hanning'):
	#	print fs,'Hz'
	dt=1.0/fs
	N=len(y)
	y=numpy.array(y)
	t=numpy.arange(0,N*dt,dt)
	freqs=numpy.arange(0,fs,fs*1.0/N)
	#y=y.mean()
	#y=scipy.signal.detrend(y)

#	fft1=numpy.fft.fft(y)/(N/2.0)
#	max(abs(fft1))
	if window=='hanning':
		window=numpy.hanning(N)
	elif window=='hft116d':
		window=hft116d(N)
	elif window=='hamming':
		window=numpy.hamming(N)
	else:
		window=numpy.ones(N)
	s1=sum(window)**2
	s2=sum(window*window)
#	print 'NENBW',N*s2/(s1**2)
#	print 'ENBW',fs*s2/(s1**2)
	fft_y_win=numpy.fft.fft(y*window)
	y_power_spectrum=2.0/s1*abs(fft_y_win)**2
	y_power_spectrum_density=2.0/s2/fs*abs(fft_y_win)**2
	return [freqs[2:N/2],y_power_spectrum[2:N/2],y_power_spectrum_density[2:N/2]]
def plot_ps_psd(freqs,ps,psd):

	pyplot.subplot(211)
	pyplot.title('linear_power_spectrum')
	lps=numpy.sqrt(ps)
	pyplot.semilogy(freqs,lps)
	print max(lps[3:-3]),max(lps[200000:300000])
	pyplot.subplot(212)
	pyplot.title('power_spectrum_density')
	lpsd=numpy.sqrt(psd)
#pyplot.semilogy(freqs,lpsd)
	pyplot.semilogy(freqs,lpsd)
	noise=lpsd[300000:400000]
	print max(lpsd[3:-3]),max(noise),noise.mean(),noise.std()
	pyplot.show()
if __name__=="__main__":
	[t,y,fs,N]=test_signal()
	[freqs,ps,psd]=ps_psd(y,fs)
	plot_ps_psd(freqs,ps,psd)
