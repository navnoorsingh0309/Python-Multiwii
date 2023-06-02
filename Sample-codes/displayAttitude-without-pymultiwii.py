import serial, struct, time

#little complicated!!! So try to understand properly

start_time = time.time()

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
#'2B' for 2 bytes of code
#we can put another data format for main data after this if we ned
#'B' for checksum

#Sending command to read attitude
serialPort.write(format_to, *total_data_to_send)

#Second step:Request -> that in inner board

#Third step:Receving data
#Untill we get $
while True:
  header = serialPort.read().decode('utf-8')
  if header=='$':
    break;
#for 'M>'
serialPort.read(2)
#length, code, data
data_length = struct.unpack('<2b', serialPort.read())
code = struct.unpack('<2b', serialPort.read())
data = serialPort.read(data_length)

#Now categorise this data in AngleX, AngleY, and Heading
unpacked_data = struct.unpack('<'+'h'*int(data_length/2), data)
#'<h3' unpack as 3 signed short integers
#/2 as there are three values in it AngleX, AngleY and Heading which are 16-bit signed integer means 2 byte. SO in total 6 bytes and 3 integerrs
#AngleX, AngleY, Heading and Some extra things
attitide['anglex'] = unpacked_data[0]
attitide['angley'] = unpacked_data[1]
attitide['heading'] = unpacked_data[2]
attitide['elapsed'] = round(time.time() - start_time, 3)
attitide['time_stamp'] = time.time()

#Attitude Prinitng
print(attitude)


#Code is not still tesed on hardware. So I am open to suggestions and errors.


