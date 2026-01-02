import numpy as np
import matplotlib.pyplot as plt
 
#---Get data---
time = np.genfromtxt('Results/Time.txt')
position = np.genfromtxt('Results/Position.txt')
velocity = np.genfromtxt('Results/Velocity.txt')
rotation = np.genfromtxt('Results/Rotation.txt')


#---Fourier transform---
#Interpolate onto a constant time step
End_Time = time[len(time)-1]
dt=0.01
t = np.arange(0, End_Time, dt)
V = np.interp(t,time,velocity-np.mean(velocity))
X = np.interp(t,time,position-np.mean(position))
#Calculate FFT
n=len(t)
FT = np.fft.fft(X)/n # Fourier coefficients (divided by n)
nu = np.fft.fftfreq(n,dt) # Natural frequencies
FT=np.fft.fftshift(FT) # Shift zero freq to center
nu= np.fft.fftshift(nu) # Shift zero freq to center
#Spectrum
Spectrum = np.absolute(FT)**2
normSpectrum = Spectrum/np.amax(Spectrum)



#---Plot----
plt.figure(1)
plt.subplot(311)
plt.plot(time, position,linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.subplot(312)
plt.plot(time, rotation,linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Pitch (deg)')
plt.subplot(313)
plt.plot(nu,normSpectrum,linewidth=2)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Spectral content')
plt.axis([0,0.2,0,1.05])
plt.show()


