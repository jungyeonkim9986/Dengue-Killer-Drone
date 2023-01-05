import serial

arduino = serial.Serial(port = 'com3', baudrate = 9600)

command = str(water_level)
arduino.write(command)