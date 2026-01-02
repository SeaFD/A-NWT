import numpy as np
import matplotlib.pyplot as plt
import os


PimpleLoops=3

#----------------------------------------------
#Get the data
#------------------------------------------
#Make Results folder to store the data
bashCommand = 'mkdir ./Results'
os.system(bashCommand)

# path to the file to read from
my_file = './log.interFoam'

#---Get Time---
# what to look in each line
look_for = 'Time ='
# variable to store time value
time = []
# fill time 
with open(my_file) as file_to_read:
	for line in file_to_read:
		if look_for in line and line.startswith('Time'):
			a=line.split('Time = ')
			time.append(a[1].strip())
#Write data to file in Results folder
outFile = open('./Results/Time.txt','w')
outFile.writelines(["%s\n" % item  for item in time])

#---Get Position---
# what to look in each line
look_for = 'Centre of rotation'
# variable to store position value
position_z = []
#Only take the value from the last Pimple iteration loop
Pimple=0
# fill position
with open(my_file) as file_to_read:
	for line in file_to_read:
		if look_for in line :
			Pimple=Pimple+1
			if Pimple == PimpleLoops:
				a=line.split()		
				position_z.append(a[5].replace(')',""))		
				Pimple=0
#Write data to file in Results folder	
outFile = open('./Results/Position.txt','w')
outFile.writelines(["%s\n" % item  for item in position_z])


#---Get Velocity---
# what to look in each line
look_for = 'Linear velocity:'
# variable to store position value
velocity = []
#Only take the value from the last Pimple iteration loop
Pimple=0
# fill velocity
with open(my_file) as file_to_read:
	for line in file_to_read:
		if look_for in line :
			Pimple=Pimple+1
			if Pimple == PimpleLoops:
				a=line.split()		
				velocity.append(a[4].replace(')',""))
				Pimple=0
outFile = open('./Results/Velocity.txt','w')
outFile.writelines(["%s\n" % item  for item in velocity])


#---Get Rotationn---
# what to look in each line
look_for = 'Orientation'
# variable to store position value
rotation_y = []
#Only take the value from the last Pimple iteration loop
Pimple=0
# fill position
with open(my_file) as file_to_read:
	for line in file_to_read:
		if look_for in line :
			Pimple=Pimple+1
			if Pimple == PimpleLoops:
				a=line.split()		
				rotation_y.append(np.degrees(np.arcsin(float(a[7])+0.25)))	
				#rotation_y.append(a[7])		
				Pimple=0
#Write data to file in Results folder	
outFile = open('./Results/Rotation.txt','w')
outFile.writelines(["%s\n" % item  for item in rotation_y])

#---Get Angular Velocity---
# what to look in each line
look_for = 'Angular velocity:'
# variable to store position value
angVelocity = []
#Only take the value from the last Pimple iteration loop
Pimple=0
# fill velocity
with open(my_file) as file_to_read:
	for line in file_to_read:
		if look_for in line :
			Pimple=Pimple+1
			if Pimple == PimpleLoops:
				a=line.split()		
				angVelocity.append(a[3])
				Pimple=0
outFile = open('./Results/angVelocity.txt','w')
outFile.writelines(["%s\n" % item  for item in angVelocity])


