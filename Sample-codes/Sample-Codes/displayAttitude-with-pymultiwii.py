from pymultiwii import Multiwii
#Serial Port (Change according to your needs)
serialPort = "dev/ttyUSB0"
#Configuring board attached to serial port
board = Multiwii(serialPort)
while True:
   #get data
   print board.getData(Multiwii.ATTITUTE)

#Output:{'timestamp': 1417432436.878697, 'elapsed': 0.016, 'angx': -26.8, 'angy': -24.8, 'heading': -84.0}
