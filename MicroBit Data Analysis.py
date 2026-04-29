"""Import packages for graphing and data analysis"""
import matplotlib.pyplot as plt
import numpy as np

"""Reading in the first data file (df1) that represents the car sitting horizontally.  
This will give us horizontal baseline values for the Microbit"""
df1 = np.transpose(np.loadtxt("HSTest_8.csv", delimiter = ",", skiprows = 1))

"""Assigning data file rows to each data logged element of the Microbit"""
HSLT = df1[1]
HSRT = df1[2]
HSLL = df1[3]
HSAx = df1[4]
HSAy = df1[5]
HSAz = df1[6]
print(len(HSLT),len(HSRT),len(HSLL),len(HSAx),len(HSAy),len(HSAz))

"""Calculate the Mean and Standard Deviation for logged data"""
AvHSAx = np.mean(HSAx)
StDvHSAx = np.std(HSAx)
AvHSAy = np.mean(HSAy)
StDvHSAy = np.std(HSAy)
AvHSAz = np.mean(HSAz)
StDvHSAz = np.std(HSAz)
print(AvHSAz,StDvHSAz)

"""Normalize the values to g = 9.81 m/s/s"""
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
    HSAcceleration_x.append(HSAx[i]*9.81/np.abs(AvHSAz))
    HSAcceleration_y.append(HSAy[i]*9.81/np.abs(AvHSAz))
    HSAcceleration_z.append(HSAz[i]*9.81/np.abs(AvHSAz))

"""Graphing data for all 3 axes of the Microbit on one graph"""
plt.figure(figsize=(10, 6))
#plt.plot(HSTime, HSAcceleration_x, 'o', color = 'r', label = 'Acceleration_x')
#plt.plot(HSTime, HSAcceleration_y, 'o', color = 'b', label = 'Acceleration_y')
#plt.plot(HSTime, HSAcceleration_z, 'o', color = 'g', label = 'Acceleration_z')
plt.plot(HSTime, HSAx, 'o', color = 'b', label = 'Acceleration_z')
plt.plot(HSTime, HSAy, 'o', color = 'r', label = 'Acceleration_z')
plt.plot(HSTime, HSAz, 'o', color = 'g', label = 'Acceleration_z')
plt.title("Horizontal Stationary Data")
plt.xlabel("Time")
plt.ylabel("Acceleration Values")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("Horizontal Stationary Data")

"""Reading in the second data file (df2) that represents the car stationary on the start ramp.  
This will give us baseline values for the Microbit on the ramp."""
df2 = np.transpose(np.loadtxt("RS1Test_8.csv", delimiter = ",", skiprows = 1))

"""Assigning data file rows to each data logged element of the Microbit"""
RS1LT = df2[1]
RS1RT = df2[2]
RS1LL = df2[3]
RS1Ax = df2[4]
RS1Ay = df2[5]
RS1Az = df2[6]
print(len(RS1LT),len(RS1RT),len(RS1LL),len(RS1Ax),len(RS1Ay),len(RS1Az))

"""Calculate the Mean and Standard Deviation for logged data"""
AvRS1Ax = np.mean(RS1Ax)
StDvRS1Ax = np.std(RS1Ax)
AvRS1Ay = np.mean(RS1Ay)
StDvRS1Ay = np.std(RS1Ay)
AvRS1Az = np.mean(RS1Az)
StDvRS1Az = np.std(RS1Az)

"""Normalize the values to g = 9.81 m/s/s"""
NRS1Ax = AvRS1Ax/np.abs(AvHSAz)*9.81
NStDvRS1Ax = StDvRS1Ax/np.abs(AvHSAz)*9.81
NRS1Ay = AvRS1Ay/np.abs(AvHSAz)*9.81
NStDvRS1Ay = StDvRS1Ay/np.abs(AvHSAz)*9.81
NRS1Az = AvRS1Az/np.abs(AvHSAz)*9.81
NStDvRS1Az = StDvRS1Az/AvHSAz*9.81

"""Perform a ramp angle check using Ax and Az"""
angle_rad1 = np.arctan(AvRS1Ax/AvRS1Az)
angle_deg1 = np.degrees(angle_rad1)
angle_rad2 = np.arctan(NRS1Ax/NRS1Az)
angle_deg2 = np.degrees(angle_rad2)

print("Ax = ",NRS1Ax," +/- ",NStDvRS1Ax," in m/s/s")
print("Ay = ",NRS1Ay," +/- ",NStDvRS1Ay," in m/s/s")
print("Az = ",NRS1Az," +/- ",NStDvRS1Az," in m/s/s")
print(angle_deg1,angle_deg2)

"""Preparing the data for graphing"""
RS1Time = []
RS1Acceleration_x = []
RS1Acceleration_y = []
RS1Acceleration_z = []
for i in list(range(0, len(df2[1]))):
    RS1Time.append((RS1RT[i] - RS1LT[i])/1000000)
    RS1Acceleration_x.append(RS1Ax[i]*9.81/np.abs(AvHSAz))
    RS1Acceleration_y.append(RS1Ay[i]*9.81/np.abs(AvHSAz))
    RS1Acceleration_z.append(RS1Az[i]*9.81/np.abs(AvHSAz))

"""Graphing data for all 3 axes of the Microbit on one graph"""
plt.figure(figsize=(10, 6))
plt.plot(RS1Time, RS1Acceleration_x, 'o', color = 'r', label = 'Acceleration_x')
plt.plot(RS1Time, RS1Acceleration_y, 'o', color = 'b', label = 'Acceleration_y')
plt.plot(RS1Time, RS1Acceleration_z, 'o', color = 'g', label = 'Acceleration_z')
plt.title("First Ramp Stationary Data")
plt.xlabel("Time")
plt.ylabel("Acceleration Values")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("First Ramp Stationary Data")

"""Reading in the third data file (df3) that represents the car stationary on the second ramp.  
This will give us baseline values for the Microbit Acclerometer on the ramp."""
df3 = np.transpose(np.loadtxt("RS2Test_8.csv", delimiter = ",", skiprows = 1))

"""Assigning data file rows to each data logged element of the Microbit"""
RS2LT = df3[1]
RS2RT = df3[2]
RS2LL = df3[3]
RS2Ax = df3[4]
RS2Ay = df3[5]
RS2Az = df3[6]
print(len(RS2LT),len(RS2RT),len(RS2LL),len(RS2Ax),len(RS2Ay),len(RS2Az))

"""Calculate the Mean and Standard Deviation for logged data"""
AvRS2Ax = np.mean(RS2Ax)
StDvRS2Ax = np.std(RS2Ax)
AvRS2Ay = np.mean(RS2Ay)
StDvRS2Ay = np.std(RS2Ay)
AvRS2Az = np.mean(RS2Az)
StDvRS2Az = np.std(RS2Az)

"""Normalize the values to g = 9.81 m/s/s"""
NRS2Ax = AvRS2Ax/np.abs(AvHSAz)*9.81
NStDvRS2Ax = StDvRS2Ax/np.abs(AvHSAz)*9.81
NRS2Ay = AvRS2Ay/np.abs(AvHSAz)*9.81
NStDvRS2Ay = StDvRS2Ay/np.abs(AvHSAz)*9.81
NRS2Az = AvRS2Az/np.abs(AvHSAz)*9.81
NStDvRS2Az = StDvRS2Az/np.abs(AvHSAz)*9.81

"""Perform a ramp angle check using Ax and Az"""
angle_rad1 = np.arctan(AvRS2Ax/AvRS2Az)
angle_deg1 = np.degrees(angle_rad1)
angle_rad2 = np.arctan(NRS2Ax/NRS2Az)
angle_deg2 = np.degrees(angle_rad2)

print("Ax = ",NRS2Ax," +/- ",NStDvRS2Ax," in m/s/s")
print("Ay = ",NRS2Ay," +/- ",NStDvRS2Ay," in m/s/s")
print("Az = ",NRS2Az," +/- ",NStDvRS2Az," in m/s/s")
print(angle_deg1,angle_deg2)

"""Preparing the data for graphing"""
RS2Time = []
RS2Acceleration_x = []
RS2Acceleration_y = []
RS2Acceleration_z = []
for i in list(range(0, len(df3[1]))):
    RS2Time.append((RS2RT[i] - RS2LT[i])/1000000)
    RS2Acceleration_x.append(RS2Ax[i]*9.81/np.abs(AvHSAz))
    RS2Acceleration_y.append(RS2Ay[i]*9.81/np.abs(AvHSAz))
    RS2Acceleration_z.append(RS2Az[i]*9.81/np.abs(AvHSAz))

"""Graphing data for all 3 axes of the Microbit on one graph"""
plt.figure(figsize=(10, 6))
plt.plot(RS2Time, RS2Acceleration_x, 'o', color = 'r', label = 'Acceleration_x')
plt.plot(RS2Time, RS2Acceleration_y, 'o', color = 'b', label = 'Acceleration_y')
plt.plot(RS2Time, RS2Acceleration_z, 'o', color = 'g', label = 'Acceleration_z')
plt.title("Second Ramp Stationary Data")
plt.xlabel("Time")
plt.ylabel("Acceleration Values")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("Second Ramp Stationary Data")

"""Reading in the fourth data file (df4) that represents the car moving on the ramp.  
This will give us values for the Microbit in motion"""
df4 = np.transpose(np.loadtxt("RMTest_8.csv", delimiter = ",", skiprows = 1))

"""Assigning data file rows to each data logged element of the Microbit"""
RMLT = df4[1]
RMRT = df4[2]
RMLL = df4[3]
RMAx = df4[4]
RMAy = df4[5]
RMAz = df4[6]
print(len(RMLT),len(RMRT),len(RMLL),len(RMAx),len(RMAy),len(RMAz))

"""Calculate the Mean and Standard Deviation for logged data"""
AvRMAx = np.mean(RMAx)
StDvRMAx = np.std(RMAx)
AvRMAy = np.mean(RMAy)
StDvRMAy = np.std(RMAy)
AvRMAz = np.mean(RMAz)
StDvRMAz = np.std(RMAz)

"""Normalize the values to g = 9.81 m/s/s"""
NRMAx = AvRMAx/np.abs(AvHSAz)*9.81
NStDvRMAx = StDvRMAx/np.abs(AvHSAz)*9.81
NRMAy = AvRMAy/np.abs(AvHSAz)*9.81
NStDvRMAy = StDvRMAy/np.abs(AvHSAz)*9.81
NRMAz = AvRMAz/np.abs(AvHSAz)*9.81
NStDvRMAz = StDvRMAz/np.abs(AvHSAz)*9.81

"""Perform a ramp angle check using Ax and Az"""
angle_rad1 = np.arctan(AvRMAx/AvRMAz)
angle_deg1 = np.degrees(angle_rad1)
angle_rad2 = np.arctan(NRMAx/NRMAz)
angle_deg2 = np.degrees(angle_rad2)

print("Ax = ",NRMAx," +/- ",NStDvRMAx," in m/s/s")
print("Ay = ",NRMAy," +/- ",NStDvRMAy," in m/s/s")
print("Az = ",NRMAz," +/- ",NStDvRMAz," in m/s/s")
print(angle_deg1,angle_deg2)

"""Preparing the data for graphing"""
RMTime = []
RMAcceleration_x = []
RMAcceleration_y = []
RMAcceleration_z = []

for i in list(range(0, len(df4[1]))):
    RMTime.append((RMRT[i] - RMLT[i])/1000000)
    RMAcceleration_x.append(RMAx[i]*9.81/np.abs(AvHSAz))
    RMAcceleration_y.append(RMAy[i]*9.81/np.abs(AvHSAz))
    RMAcceleration_z.append(RMAz[i]*9.81/np.abs(AvHSAz))
    
# Plot the data for the Accelerometer x-Axis
plt.figure(figsize=(10, 6))
plt.plot(RMTime, RS1Acceleration_x, 'o', color = 'b', label = 'Ramp 1 Acceleration_x') # You can change 'marker' or chart type (e.g., plt.bar for bar chart)
plt.plot(RMTime, RS2Acceleration_x, 'o', color = 'r', label = 'Ramp 2 Acceleration_x')
plt.plot(RMTime, RMAcceleration_x, 'o', color = 'g', label = 'Moving Acceleration_x')
plt.title("Accelerometer in Motion Ax")
plt.xlabel("Time")
plt.ylabel("Acceleration x")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("Accelerometer in Motion Ax")

# Plot the data for the Accelerometer z-Axis
plt.figure(figsize=(10, 6))
plt.plot(RMTime, RS1Acceleration_z, 'o', color = 'b', label = 'Ramp 1 Acceleration_z') # You can change 'marker' or chart type (e.g., plt.bar for bar chart)
plt.plot(RMTime, RS2Acceleration_z, 'o', color = 'r', label = 'Ramp 2 Acceleration_z')
plt.plot(RMTime, RMAcceleration_z, 'o', color = 'g', label = 'Moving Acceleration_z')
plt.title("Accelerometer in Motion Az")
plt.xlabel("Time")
plt.ylabel("Acceleration z")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("Accelerometer in Motion Az")

# Determining the occurences of light level values greater than 253 
LL = []
index = []
for i in range(0, len(RMLL)):
    if RMLL[i] >= 253:
        LL.append(RMLL[i])
        index.append(i)
index.append(0)

# Determining data boundaries using the occurences of maximum light levels
wdth = []
bounds = []
bounds_i = []
for i in range(0, (len(index)-1)):
    check1 = index[i]
    check2 = index[i+1]
    check = check2 - check1
    if check == 1:
        wdth.append(index[i])
    if check != 1:
        wdth.append(index[i])
        cntr = np.rint(np.mean(wdth))
        bounds.append(cntr)
        wdth.clear()
bounds_i = np.round(bounds).astype(int)

# Setting up data for Ax and Az using the determined boundaries
time_ax = []
theoretical_ax = []
actual_ax = []
noise_ax = []
#time_az = []
#theoretical_az = []
#actual_az = []
#noise_az = []
for i in range(0, bounds_i[3]):
    if i>=0 and i<=bounds[0]:
        time_ax.append(RMTime[i])
        theoretical_ax.append(NRS1Ax)
        actual_ax.append(RMAcceleration_x[i])
        noise_ax.append(RMAcceleration_x[i]-NRS1Ax)
        #time_az.append(RMTime[i])
        #theoretical_az.append(NRS1Az)
        #actual_az.append(RMAcceleration_z[i])
        #noise_az.append(RMAcceleration_z[i]-NRS1Az)
    if i>=bounds[0] and i<=bounds[1]:
        time_ax.append(RMTime[i])
        theoretical_ax.append(NRS2Ax)
        actual_ax.append(RMAcceleration_x[i])
        noise_ax.append(RMAcceleration_x[i]-NRS2Ax)
        #time_az.append(RMTime[i])
        #theoretical_az.append(NRS2Az)
        #actual_az.append(RMAcceleration_z[i])
        #noise_az.append(RMAcceleration_z[i]-NRS2Az)
    if i>=bounds[1] and i<=bounds[2]:
        time_ax.append(RMTime[i])
        theoretical_ax.append(NRS1Ax)
        actual_ax.append(RMAcceleration_x[i])
        noise_ax.append(RMAcceleration_x[i]-NRS1Ax)
        #time_az.append(RMTime[i])
        #theoretical_az.append(NRS1Az)
        #actual_az.append(RMAcceleration_z[i])
        #noise_az.append(RMAcceleration_z[i]-NRS1Az)
    if i>=bounds[2] and i<=bounds[3]:
        time_ax.append(RMTime[i])
        theoretical_ax.append(NRS2Ax)
        actual_ax.append(RMAcceleration_x[i])
        noise_ax.append(RMAcceleration_x[i]-NRS2Ax)
        #time_az.append(RMTime[i])
        #theoretical_az.append(NRS2Az)
        #actual_az.append(RMAcceleration_z[i])
        #noise_az.append(RMAcceleration_z[i]-NRS2Az)



# Determing Velocity values using Trapezoid method of Integration
time_vx = []
theoretical_vx = []
riem_vx = 0
#time_vz = []
#theoretical_vz = []
#riem_vz = 0
for i in range(0, (len(time_ax)-1)):
    trap_ax = 0.5*(theoretical_ax[i] + theoretical_ax[i+1])*(time_ax[i+1] - time_ax[i])
    intime_ax = 0.5*(time_ax[i+1] + time_ax[i])
    riem_vx = riem_vx + trap_ax
    theoretical_vx.append(riem_vx)
    time_vx.append(intime_ax)
    #trap_az = 0.5*(theoretical_az[i] + theoretical_az[i+1])*(time_ax[i+1] - time_ax[i])
    #intime_az = 0.5*(time_ax[i+1] + time_ax[i])
    #riem_vz = riem_vz + trap_az
    #theoretical_vz.append(riem_vz)
    #time_vz.append(intime_az)

# Determing Position values using Trapezoid method of Integration
time_px = []
theoretical_px = []
riem_px = 0
time_pz = []
theoretical_pz = []
riem_pz = 0
for i in range(0, (len(time_vx)-1)):
    trap_vx = 0.5*(theoretical_vx[i] + theoretical_vx[i+1])*(time_vx[i+1] - time_vx[i])
    intime_vx = 0.5*(time_vx[i+1] + time_vx[i])
    riem_px = riem_px + trap_vx
    theoretical_px.append(riem_px)
    time_px.append(intime_vx)
    #trap_vz = 0.5*(theoretical_vz[i] + theoretical_vz[i+1])*(time_vx[i+1] - time_vx[i])
    #intime_vz = 0.5*(time_vx[i+1] + time_vx[i])
    #riem_pz = riem_pz + trap_vz
    #theoretical_pz.append(riem_pz)
    #time_pz.append(intime_vz)

# Plot the data for the Theoretical Accelerometer x-Axis
plt.figure(figsize=(10, 6))
plt.plot(time_ax, theoretical_ax, 'o', color = 'b', label = 'Theoretical Acceleration')
plt.title("Theoretical Accelerometer in Motion Ax")
plt.xlabel("Time")
plt.ylabel("Acceleration x")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("Theoretical Accelerometer in Motion Ax")

# Plot the data for the Theoretical Accelerometer z-Axis
#plt.figure(figsize=(10, 6))
#plt.plot(time_az, theoretical_az, 'o', color = 'b', label = 'Theoretical Acceleration')
#plt.title("Theoretical Accelerometer in Motion Az")
#plt.xlabel("Time")
#plt.ylabel("Acceleration z")
#plt.legend()
#plt.grid(True)
#plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
#plt.tight_layout() # Adjust layout to prevent clipping of labels
#plt.savefig("Theoretical Accelerometer in Motion Az")

# Plot the data for the Theoretical Velocity x-Axis
plt.figure(figsize=(10, 6))
plt.plot(time_vx, theoretical_vx, 'o', color = 'b', label = 'Theoretical Velocity')
plt.title("Theoretical Velocity in Motion Ax")
plt.xlabel("Time")
plt.ylabel("Velocity x")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("Theoretical Velocity in Motion Ax")

# Plot the data for the Theoretical Velocity z-Axis
#plt.figure(figsize=(10, 6))
#plt.plot(time_vz, theoretical_vz, 'o', color = 'b', label = 'Theoretical Velocity')
#plt.title("Theoretical Velocity in Motion Az")
#plt.xlabel("Time")
#plt.ylabel("Velocity z")
#plt.legend()
#plt.grid(True)
#plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
#plt.tight_layout() # Adjust layout to prevent clipping of labels
#plt.savefig("Theoretical Velocity in Motion Az")

# Plot the data for the Theoretical Position x-Axis
plt.figure(figsize=(10, 6))
plt.plot(time_px, theoretical_px, 'o', color = 'b', label = 'Theoretical Velocity')
plt.title("Theoretical Position in Motion Ax")
plt.xlabel("Time")
plt.ylabel("Position x")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("Theoretical Position in Motion Ax")

# Plot the data for the Theoetical Position z-Axis
#plt.figure(figsize=(10, 6))
#plt.plot(time_pz, theoretical_pz, 'o', color = 'b', label = 'Theoretical Velocity')
#plt.title("Theoretical Position in Motion Az")
#plt.xlabel("Time")
#plt.ylabel("Position z")
#plt.legend()
#plt.grid(True)
#plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
#plt.tight_layout() # Adjust layout to prevent clipping of labels
#plt.savefig("Theoretical Position in Motion Az")

# Plot the data for the Actual Accelerometer x-Axis
plt.figure(figsize=(10, 6))
plt.plot(time_ax, actual_ax, 'o', color = 'g', label = 'Actual Acceleration')
plt.title("Actual Accelerometer in Motion Ax")
plt.xlabel("Time")
plt.ylabel("Acceleration x")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("Actual Accelerometer in Motion Ax")

# Plot the data for the Actual Accelerometer z-Axis
#plt.figure(figsize=(10, 6))
#plt.plot(time_az, actual_az, 'o', color = 'g', label = 'Actual Acceleration')
#plt.title("Actual Accelerometer in Motion Az")
#plt.xlabel("Time")
#plt.ylabel("Acceleration z")
#plt.legend()
#plt.grid(True)
#plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
#plt.tight_layout() # Adjust layout to prevent clipping of labels
#plt.savefig("Actual Accelerometer in Motion Az")

# Plot the data for the Theoretical Accelerometer x-Axis with noise
plt.figure(figsize=(10, 6))
plt.plot(time_ax, theoretical_ax, 'o', color = 'b', label = 'Theoretical Acceleration')
plt.plot(time_ax, noise_ax, 'o', color = 'g', label = 'Noise')
plt.title("Theoretical with Noise Accelerometer in Motion Ax")
plt.xlabel("Time")
plt.ylabel("Acceleration x")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.savefig("Theoretical with Noise Accelerometer in Motion Ax")

# Plot the data for the Theoretical Accelerometer z-Axis with noise
#plt.figure(figsize=(10, 6))
#plt.plot(time_az, theoretical_az, 'o', color = 'b', label = 'Theoretical Acceleration')
#plt.plot(time_az, noise_az, 'o', color = 'g', label = 'Noise')
#plt.title("Theoretical with Noise Accelerometer in Motion Az")
#plt.xlabel("Time")
#plt.ylabel("Acceleration z")
#plt.legend()
#plt.grid(True)
#plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
#plt.tight_layout() # Adjust layout to prevent clipping of labels
#plt.savefig("Theoretical with Noise Accelerometer in Motion Ax")



# Output time_ax and theoretical_ax to a two-column CSV file
time_theoretical_ax_data = np.column_stack((time_ax, theoretical_ax))
np.savetxt(
    "time_theoretical_ax.csv",
    time_theoretical_ax_data,
    delimiter=",",
    header="time_ax,theoretical_ax",
    comments="",
    fmt="%.18g"
)

velocity_theoretical_vx_data = np.column_stack((time_vx, theoretical_vx))
np.savetxt(
    "velocity_theoretical_vx.csv",
    velocity_theoretical_vx_data,
    delimiter=",",
    header="time_ax,theoretical_vx",
    comments="",
    fmt="%.18g"
)

position_theoretical_px_data = np.column_stack((time_px, theoretical_px))
np.savetxt(
    "position_theoretical_px.csv",
    position_theoretical_px_data,
    delimiter=",",
    header="time_px,theoretical_px",
    comments="",
    fmt="%.18g"
)
