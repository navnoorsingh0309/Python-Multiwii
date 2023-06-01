#Python Multiwii


pymultiwii is used to handle multiwii serial protocol to send/receieve data from boards accesed with multiwii.

It read data or send commands from your pc thorugh serial communication. You can control your multirotar platform wirelessly using boards like raspberry pi, flight controller, etc.

##Installation

To install pymultiwii usinf pip, run the following command:

```
pip install multiwii
```

#Multwii Serial Protocol(MSP)

Format of MSP is:
```
$<preamble><direction><size><code><data><checksum>$
```
Premable = '$M'(2 bytes)
Direction = '<' or '>' for data receiving and sending.
Size = its data length
code = message_id as per link
data = as per link
checksum = XOR of <size>, <code>
  
http://www.multiwii.com/wiki/index.php?title=Multiwii_Serial_Protocol

###How data flow happens?

Communication is operated using Master/Slave Technology. There are devices which act as 'Master' and send command/data to 'Slave' device. Some devices at as both 'Master' and 'Slave' depending on situation, like in this while sending our PC is 'Master' and board is 'Slave' and while receiving roles interchange.
'Master' interacts with 'Slave' in this case with three types of messages. These messages are: 
1. Command-Incoming message
2. Request-Incoming message with implicit outgoing response
3. Response-Outgoing response

#Some Samples
  
###Receiving Data

Create Multiwii object that receives data from the serial port mentioned by using getData function:
```
from pymultiwii import Multiwii

serialPort = "/dev/ttyUSB0"
board = Multiwii(serialPort)
while True:
    print board.getData(Multiwii.ATTITUTE)
```
You can also do this without 'pymultiwii' library
```
import serial
import time
#Configure Serial port
port = 'COM4'   #Repalce with correct port
baudrate = 115200    #Baudrate-speed of data transmittion

#Open the serial connection
serialP = serial.Serial(port, baudrate, timeout=1)

#Rading Data
def read_Data():
    while True:    #When get
        if serialP.read()==b'$'   #$ in byte format
            header = serialP.read(2)
            if 
