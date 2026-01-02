import pandas as pd
import matplotlib.pyplot as plt
# Load the data from the file
file_path = 'postProcessing/interfaceHeight1/0/height.dat'
data = pd.read_csv(file_path, delimiter='\s+')
# Extract the necessary columns into vectors
Time = data.iloc[:, 0]
WG60 = data.iloc[:, 1]
WG120 = data.iloc[:, 3]
WG180 = data.iloc[:, 5]
initialHeight=WG60[0] #To zero the initial height in the plots
# Plot the data in two subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 8))
# First subplot: Time vs WG1
axs[0].plot(Time, WG60-initialHeight, label='WG60', color='b')
axs[0].set_xlabel('Time [s]')
axs[0].set_ylabel('Free Surface Elevation [m]')
axs[0].set_title('WG60')
axs[0].legend()
# Second subplot: Time vs WG120
axs[1].plot(Time, WG120-initialHeight, label='WG120', color='b')
axs[1].set_xlabel('Time [s]')
axs[1].set_ylabel('Free Surface Elevation [m]')
axs[1].set_title('WG120')
axs[1].legend()
#Third subplot: Time vs WG120
axs[2].plot(Time, WG180-initialHeight, label='WG180', color='b')
axs[2].set_xlabel('Time [s]')
axs[2].set_ylabel('Free Surface Elevation [m]')
axs[2].set_title('WG180')
axs[2].legend()
# Adjust layout
plt.tight_layout()
# Show the plot
plt.show()

outFile = open('./Time.txt','w') #Write data to file 
outFile.writelines(["%s\n" % item  for item in Time])
outFile = open('./WG60.txt','w') 
outFile.writelines(["%s\n" % item  for item in WG60])
outFile = open('./WG120.txt','w') 	
outFile.writelines(["%s\n" % item  for item in WG120])
outFile = open('./WG180.txt','w') 	
outFile.writelines(["%s\n" % item  for item in WG180])

