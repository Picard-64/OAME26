"""Import packages for graphing and data analysis"""
import matplotlib.pyplot as plt
import numpy as np

"""Reading in the first data file (df1) that represnets the car sitting horizontally.  
This will give us baseline values for the Microbit Acclerometer"""
df1 = np.transpose(np.loadtxt("HSTest_9.csv", delimiter = ",", skiprows = 1))

"""Assigning data file rows to each axis of the Microbit Accelerometer"""
HSLT = df1[1]
HSRT = df1[2]
HSLL = df1[3]
HSAx = df1[4]
HSAy = df1[5]
HSAz = df1[6]
print(len(HSLT),len(HSRT),len(HSAx),len(HSAy),len(HSAz))

"""Calculate the Mean and Standard Deviation for each axis of the accelerometer"""
AvHSAx = np.mean(HSAx)
StDvHSAx = np.std(HSAx)
AvHSAy = np.mean(HSAy)
StDvHSAy = np.std(HSAy)
AvHSAz = np.mean(HSAz)
StDvHSAz = np.std(HSAz)

"""Normalize the values to m/s/s"""
NHSAx = AvHSAx/np.abs(AvHSAz)*9.81
NStDvHSAx = StDvHSAx/np.abs(AvHSAz)*9.81
NHSAy = AvHSAy/np.abs(AvHSAz)*9.81
NStDvHSAy = StDvHSAy/np.abs(AvHSAz)*9.81
NHSAz = AvHSAz/np.abs(AvHSAz)*9.81
NStDvHSAz = StDvHSAz/np.abs(AvHSAz)*9.81

"""Perform an angle check using Ax and Az"""
angle_rad1 = np.arctan(AvHSAx/AvHSAz)
angle_deg1 = np.degrees(angle_rad1)
angle_rad2 = np.arctan(NHSAx/NHSAz)
angle_deg2 = np.degrees(angle_rad2)

print("Ax = ",NHSAx," +/- ",NStDvHSAx," in m/s/s")
print("Ay = ",NHSAy," +/- ",NStDvHSAy," in m/s/s")
print("Az = ",NHSAz," +/- ",NStDvHSAz," in m/s/s")
print(angle_deg1,angle_deg2)

"""Preparing the data for graphing"""
HSTime = []
HSAcceleration_x = []
HSAcceleration_y = []
HSAcceleration_z = []
for i in list(range(0, len(df1[1]))):
    HSTime.append((HSRT[i] - HSLT[i])/1000000)
    HSAcceleration_x.append((HSAx[i]*9.81/AvHSAz))
    HSAcceleration_y.append((HSAy[i]*9.81/AvHSAz))
    HSAcceleration_z.append((HSAz[i]*9.81/AvHSAz))

"""Graphing data for all 3 axes of the accelerometer on one graph"""
plt.figure(figsize=(10, 6))
plt.plot(HSTime, HSAcceleration_x, 'o', color = 'r', label = 'Acceleration_x')
plt.plot(HSTime, HSAcceleration_y, 'o', color = 'b', label = 'Acceleration_y')
plt.plot(HSTime, HSAcceleration_z, 'o', color = 'g', label = 'Acceleration_z')
plt.title("Horizontal Stationary Data")
plt.xlabel("Time")
plt.ylabel("Acceleration")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("Horizontal Stationary Data")

"""Reading in the second data file (df2) that represnets the car stationary on the ramp.  
This will give us baseline values for the Microbit Acclerometer on the ramp."""
df2 = np.transpose(np.loadtxt("RSTest_9.csv", delimiter = ",", skiprows = 1))

"""Assigning data file rows to each axis of the Microbit Accelerometer"""
RSLT = df2[1]
RSRT = df2[2]
RSLL = df2[3]
RSAx = df2[4]
RSAy = df2[5]
RSAz = df2[6]
print(len(RSLT),len(RSRT),len(RSAx),len(RSAy),len(RSAz))
"""Calculate the Mean and Standard Deviation for each axis of the accelerometer"""
AvRSAx = np.mean(RSAx)
StDvRSAx = np.std(RSAx)
AvRSAy = np.mean(RSAy)
StDvRSAy = np.std(RSAy)
AvRSAz = np.mean(RSAz)
StDvRSAz = np.std(RSAz)

"""Normalize the values to m/s/s"""
NRSAx = AvRSAx/np.abs(AvHSAz)*9.81
NStDvRSAx = StDvRSAx/np.abs(AvHSAz)*9.81
NRSAy = AvRSAy/np.abs(AvHSAz)*9.81
NStDvRSAy = StDvRSAy/np.abs(AvHSAz)*9.81
NRSAz = AvRSAz/np.abs(AvHSAz)*9.81
NStDvRSAz = StDvRSAz/np.abs(AvHSAz)*9.81

"""Perform a ramp angle check using Ax and Az"""
angle_rad1 = np.arctan(AvRSAx/AvRSAz)
angle_deg1 = np.degrees(angle_rad1)
angle_rad2 = np.arctan(NRSAx/NRSAz)
angle_deg2 = np.degrees(angle_rad2)

print("Ax = ",NRSAx," +/- ",NStDvRSAx," in m/s/s")
print("Ay = ",NRSAy," +/- ",NStDvRSAy," in m/s/s")
print("Az = ",NRSAz," +/- ",NStDvRSAz," in m/s/s")
print(angle_deg1,angle_deg2)

"""Preparing the data for graphing"""
RSTime = []
RSAcceleration_x = []
RSAvAcceleration_x = []
RSAcceleration_y = []
RSAcceleration_z = []
for i in list(range(0, len(df2[1]))):
    RSTime.append((RSRT[i] - RSLT[i])/1000000)
    RSAcceleration_x.append((RSAx[i]*9.81/np.abs(AvHSAz)))
    RSAvAcceleration_x.append(NRSAx)
    RSAcceleration_y.append((RSAy[i]*9.81/AvHSAz))
    RSAcceleration_z.append((RSAz[i]*9.81/AvHSAz))

"""Graphing data for all 3 axes of the accelerometer on one graph"""
plt.figure(figsize=(10, 6))
plt.plot(RSTime, RSAcceleration_x, 'o', color = 'r', label = 'Acceleration_x')
plt.plot(RSTime, RSAcceleration_y, 'o', color = 'b', label = 'Acceleration_y')
plt.plot(RSTime, RSAcceleration_z, 'o', color = 'g', label = 'Acceleration_z')
plt.title("Ramp Stationary Data")
plt.xlabel("Time")
plt.ylabel("Acceleration")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("Ramp Stationary Data")

"""Reading in the third data file (df3) that represnets the car moving on the ramp.  
This will give us values for the Microbit Acclerometer in motion"""
df3 = np.transpose(np.loadtxt("RMTest_9.csv", delimiter = ",", skiprows = 1))

"""Assigning data file rows to each axis of the Microbit Accelerometer"""
RMLT = df3[1]
RMRT = df3[2]
RMLL = df3[3]
RMAx = df3[4]
RMAy = df3[5]
RMAz = df3[6]
print(len(RMLT),len(RMRT),len(RMAx),len(RMAy),len(RMAz))
"""Preparing the data for graphing"""
RMTime = []
RMAcceleration_x = []
RMAcceleration_y = []
RMAcceleration_z = []

for i in list(range(0, len(df3[1]))):
    RMTime.append((RMRT[i] - RMLT[i])/1000000)
    RMAcceleration_x.append((RMAx[i]*9.81/AvHSAz))
    RMAcceleration_y.append((RMAy[i]*9.81/AvHSAz))
    RMAcceleration_z.append((RMAz[i]*9.81/AvHSAz))

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(RMTime, RMAcceleration_x, 'o', color = 'b', label = 'Moving Acceleration_x') # You can change 'marker' or chart type (e.g., plt.bar for bar chart)
plt.plot(RMTime, RSAcceleration_x, 'o', color = 'r', label = 'Stationary Acceleration_x')
plt.plot(RMTime, RSAvAcceleration_x, 'o', color = 'g', label = 'Average Stationary Acceleration_x')
plt.title("Accelerometer in Motion Ax")
plt.xlabel("Time")
plt.ylabel("Acceleration x")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("Accelerometer in Motion Ax")

"""plt.figure(figsize=(10, 6))
plt.plot(RMTime, RMAcceleration_y, 'o', color = 'b', label = 'Acceleration_y') # You can change 'marker' or chart type (e.g., plt.bar for bar chart)
plt.title("Accelerometer in Motion Ay")
plt.xlabel("Time")
plt.ylabel("Acceleration y")
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("Accelerometer in Motion Ay")"

plt.figure(figsize=(10, 6))
plt.plot(RMTime, RMAcceleration_z, 'o', color = 'b', label = 'Acceleration_z') # You can change 'marker' or chart type (e.g., plt.bar for bar chart)
plt.title("Accelerometer in Motion Az")
plt.xlabel("Time")
plt.ylabel("Acceleration z")
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("Accelerometer in Motion Az")"""

window_size = 8
RMTime_8_1 = np.convolve(RMTime, np.ones(window_size)/window_size, mode = 'valid')
RMAccelerationx_8_1 = np.convolve(RMAcceleration_x, np.ones(window_size)/window_size, mode = 'valid')
RSAccelerationx_8_1 = np.convolve(RSAvAcceleration_x, np.ones(window_size)/window_size, mode = 'valid')
RMAccelerationy_8_1 = np.convolve(RMAcceleration_y, np.ones(window_size)/window_size, mode = 'valid')
RMAccelerationz_8_1 = np.convolve(RMAcceleration_z, np.ones(window_size)/window_size, mode = 'valid')
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(RMTime_8_1, RMAccelerationx_8_1, 'o', color = 'b', label = 'Moving Acceleration_x')
plt.plot(RMTime_8_1, RSAccelerationx_8_1, 'o', color = 'r', label = 'Average Stationary Acceleration_x')
plt.title("Accelerometer in Motion Ax Rolling Average Window Size 8 Pass 1")
plt.xlabel("Time")
plt.ylabel("Acceleration x")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("Window Size 8 Pass 1")

window_size = 8
RMTime_8_2 = np.convolve(RMTime_8_1, np.ones(window_size)/window_size, mode = 'valid')
RMAccelerationx_8_2 = np.convolve(RMAccelerationx_8_1, np.ones(window_size)/window_size, mode = 'valid')
RSAccelerationx_8_2 = np.convolve(RSAccelerationx_8_1, np.ones(window_size)/window_size, mode = 'valid')
RMAccelerationy_8_2 = np.convolve(RMAccelerationy_8_1, np.ones(window_size)/window_size, mode = 'valid')
RMAccelerationz_8_2 = np.convolve(RMAccelerationz_8_1, np.ones(window_size)/window_size, mode = 'valid')
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(RMTime_8_2, RMAccelerationx_8_2, 'o', color = 'b', label = 'Moving Acceleration_x')
plt.plot(RMTime_8_2, RSAccelerationx_8_2, 'o', color = 'r', label = 'Average Stationary Acceleration_x')
plt.title("Accelerometer in Motion Ax Rolling Average Window Size 8 Pass 2")
plt.xlabel("Time")
plt.ylabel("Acceleration x")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("Window Size 8 Pass 2")

window_size = 8
RMTime_8_3 = np.convolve(RMTime_8_2, np.ones(window_size)/window_size, mode = 'valid')
RMAccelerationx_8_3 = np.convolve(RMAccelerationx_8_2, np.ones(window_size)/window_size, mode = 'valid')
RSAccelerationx_8_3 = np.convolve(RSAccelerationx_8_2, np.ones(window_size)/window_size, mode = 'valid')
RMAccelerationy_8_3 = np.convolve(RMAccelerationy_8_2, np.ones(window_size)/window_size, mode = 'valid')
RMAccelerationz_8_3 = np.convolve(RMAccelerationz_8_2, np.ones(window_size)/window_size, mode = 'valid')
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(RMTime_8_3, RMAccelerationx_8_3, 'o', color = 'b', label = 'Moving Acceleration_x')
plt.plot(RMTime_8_3, RSAccelerationx_8_3, 'o', color = 'r', label = 'Average Stationary Acceleration_x')
plt.title("Accelerometer in Motion Ax Rolling Average Window Size 8 Pass 3")
plt.xlabel("Time")
plt.ylabel("Acceleration x")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("Window Size 8 Pass 3")

window_size = 8
RMTime_8_4 = np.convolve(RMTime_8_3, np.ones(window_size)/window_size, mode = 'valid')
RMAccelerationx_8_4 = np.convolve(RMAccelerationx_8_3, np.ones(window_size)/window_size, mode = 'valid')
RSAccelerationx_8_4 = np.convolve(RSAccelerationx_8_3, np.ones(window_size)/window_size, mode = 'valid')
RMAccelerationy_8_4 = np.convolve(RMAccelerationy_8_3, np.ones(window_size)/window_size, mode = 'valid')
RMAccelerationz_8_4 = np.convolve(RMAccelerationz_8_3, np.ones(window_size)/window_size, mode = 'valid')
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(RMTime_8_4, RMAccelerationx_8_4, 'o', color = 'b', label = 'Moving Acceleration_x')
plt.plot(RMTime_8_4, RSAccelerationx_8_4, 'o', color = 'r', label = 'Average Stationary Acceleration_x')
plt.title("Accelerometer in Motion Ax Rolling Average Window Size 8 Pass 4")
plt.xlabel("Time")
plt.ylabel("Acceleration x")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("Window Size 8 Pass 4")

window_size = 8
RMTime_8_5 = np.convolve(RMTime_8_4, np.ones(window_size)/window_size, mode = 'valid')
RMAccelerationx_8_5 = np.convolve(RMAccelerationx_8_4, np.ones(window_size)/window_size, mode = 'valid')
RSAccelerationx_8_5 = np.convolve(RSAccelerationx_8_4, np.ones(window_size)/window_size, mode = 'valid')
RMAccelerationy_8_5 = np.convolve(RMAccelerationy_8_4, np.ones(window_size)/window_size, mode = 'valid')
RMAccelerationz_8_5 = np.convolve(RMAccelerationz_8_4, np.ones(window_size)/window_size, mode = 'valid')
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(RMTime_8_5, RMAccelerationx_8_5, 'o', color = 'b', label = 'Moving Acceleration_x')
plt.plot(RMTime_8_5, RSAccelerationx_8_5, 'o', color = 'r', label = 'Average Stationary Acceleration_x')
plt.title("Accelerometer in Motion Ax Rolling Average Window Size 8 Pass 5")
plt.xlabel("Time")
plt.ylabel("Acceleration x")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("Window Size 8 Pass 5")

window_size = 8
RMTime_8_6 = np.convolve(RMTime_8_5, np.ones(window_size)/window_size, mode = 'valid')
RMAccelerationx_8_6 = np.convolve(RMAccelerationx_8_5, np.ones(window_size)/window_size, mode = 'valid')
RSAccelerationx_8_6 = np.convolve(RSAccelerationx_8_5, np.ones(window_size)/window_size, mode = 'valid')
RMAccelerationy_8_6 = np.convolve(RMAccelerationy_8_5, np.ones(window_size)/window_size, mode = 'valid')
RMAccelerationz_8_6 = np.convolve(RMAccelerationz_8_5, np.ones(window_size)/window_size, mode = 'valid')
# Plot the data
plt.figure(figsize=(10, 6))
#plt.plot(RMTime_8_6, RMAccelerationx_8_6, 'o', color = 'b', label = 'Moving Acceleration_x')
plt.plot(RMTime_8_6, RSAccelerationx_8_6, 'o', color = 'r', label = 'Acceleration#')
#plt.title("Accelerometer in Motion Ax Rolling Average Window Size 8 Pass 6")
plt.xlabel("Time")
plt.ylabel("Acceleration x")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("Window Size 8 Pass 6")