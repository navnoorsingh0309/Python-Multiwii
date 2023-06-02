import serial, struct, time

#Serial Connections
serialPortName = "/dev/ttyUSB0"
serialPort= serial.Serial(serialPortName, baudrate=115200)

#--------Arm Drone-----------
#Code=200 for Dronw MSP.SET_RAW_RC
#8 RC Channels for Drone(Specifically Pluto Drones)
# 1. Roll
# 2. Pitch
# 3. Yaw
# 4. Throttle
# 5. AUX1
# 6. AUX2
# 7. AUX3
# 8. AUX4
# AUX4=1500 for arming and AUX4=0 for disarming
#data to send
data = [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500]

#as it is uint_16 (8 unsigned integers - 2 byte)
data_length = len(data)*2
#h-unsigned integer and * 8  as 8 unsigned integer with little ending-'<'
data_format = '8H'
#code for arming
code_arm = 200

#Total_Data
total_data = ['$'.encode('utf-8'), 'M'.encode('utf-8'), '<'.encode('utf-8'), data_length, code_arm] + data

#Checksum
checksum = 0
#Loop for length and code
for i in struct.pack('<3c2B'+data_fromat+'B', *total_data[3:len(total_data)]):
  checksum = checksum ^ i   #XOR of total_length and command

#Appending the checksum
total_data.append(checksum)
#Sending Command to Arm
serialPort.write(struct.pack('<3c2B'+data_format+'B', *total_data))


#Take-Off
#MSP_SET_COMMAND=217
data_for_takeoff = 
