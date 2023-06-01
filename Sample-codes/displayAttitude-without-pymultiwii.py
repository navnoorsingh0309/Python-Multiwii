import serial, struct

#little complicated!!! So try to understand properly

serialPortName = "/dev/ttyUSB0" # change serial port accordingly
serialPort = serial.Serial(serialPortName, baudrate=115200) #initializing Serial Communication Port

#First step: Sending Command
#$M<(Length)(Command)(Data)(Checksum)
#108 code for attitude
#0 length
#and [] empty data as we need data from drone
total_data_to_send = ['$'.encode('utf-8'), 'M'.encode('utf-8'), '<'.encode('utf-8'), 0, 108]+[]
checksum = 0
#'<2B' means packing 2 unsigned bytes
# '*' before list convert that one list to two byte data (0, 108) to pack
for i in struct.pack('<2B', *total_data_to_send[3:len(total_data_to_send)]):
  checksum = checksum ^ i  #XOR with length and code
  #in above code i will be 0 and 108 respectively in 2 iterations
total_data_to_send.append(checksum)

format_to = '<3c2BB'
#'<' little endian byte order
#'3c' for 3 character(3  bytes) [$M<]
#'2B' for 2 bytes of length and code
#we can put another data format for main data after this if we ned
#'B' for checksum

#Sending command to read attitude
serialPort.write(format_to, *total_data_to_send)

#Second step:Request -> that in inner board

#Third step:Receving data
