import serial
import water_detection as wd
from wd import water_level

arduino = serial.Serial(port = 'com3', baudrate = 9600)

command = str(water_level)
arduino.write(command)
