# Rybuck v01
# Program sprawdza reakcje klienta na klikniecie klawiatury

import serial
import time
BUFF = 255

ser = serial.Serial(port='COM4')
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.timeout = 1
print('serial opened')
print(f'PORT:     {ser.port}')
print(f'BAUD:     {ser.baudrate}')
print(f'SIZE:     {ser.bytesize}')
print(f'PARITY:   {ser.parity}')
print(f'STOPBITS: {ser.stopbits}')
print(f'TIMEOUT:  {ser.timeout}')


while True:
    echo = ser.read(BUFF)
    # echo = echo.decode()
    if len(echo):
        print(echo)
    command = str(input())
    time.sleep(2)
    if command:
        command = command + '\n'
        ser.write(command.encode())



