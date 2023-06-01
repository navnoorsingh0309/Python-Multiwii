from pymultiwii import Multiwii
serialPort = "dev/ttyUSB0"
board = Multiwii(serialPort)
while True:
   print board.getData(Multiwii.ATTITUTE)

#Output:{'timestamp': 1417432436.878697, 'elapsed': 0.016, 'angx': -26.8, 'angy': -24.8, 'heading': -84.0}
