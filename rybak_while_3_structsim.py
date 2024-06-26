import statistics

import numpy as np
import pyautogui
import cv2
import serial
import time
import random
from skimage.metrics import structural_similarity

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

images_to_compare = []
image_loaded = np.array(cv2.imread('data/pic4.jpg'))
image_compared = cv2.cvtColor(image_loaded, cv2.COLOR_RGB2GRAY)
for _ in range(0, 5):
    image_loaded = cv2.imread(f'data/pic{_}.jpg')
    images_to_compare.append(cv2.cvtColor(image_loaded, cv2.COLOR_RGB2GRAY))
not_taking_out = True

i = 0
while True:
    image = 0
    image_matrix = 0
    image_gray = 0
    image = pyautogui.screenshot(region=(960, 390, 120, 120))
    image_matrix = np.array(image)
    image_gray = cv2.cvtColor(image_matrix, cv2.COLOR_RGB2GRAY)
    cv2.imwrite('raw_data/test.jpg', image_gray)
    time.sleep(0.2)
    struct_similarity, diff = structural_similarity(image_gray, image_compared, full=True)
    # print(struct_similarity)
    results = []
    if struct_similarity > 0.4:
        for _ in range(0,5):
            image_to_compare = images_to_compare[_]
            smoke_similarity = structural_similarity(image_gray, image_to_compare)
            print(f'podobienstwo {smoke_similarity} do pic{_}')
            if smoke_similarity > 0.70:
                result = _ + 1
                print(result)
                recognition_delay = 0.766 + random.random()
                time.sleep(recognition_delay)
                print(f'po rozpoznaniu {recognition_delay}sek')
                command = str(result) + '\n'
                ser.write(command.encode())
                bait_delay = 10 + (2 * random.random())
                time.sleep(bait_delay)
                print(f'robak {bait_delay}sek')
                command = 'r' + '\n'
                ser.write(command.encode())
                rod_delay = 1.5 + random.random()
                time.sleep(rod_delay)
                print(f'wedka{rod_delay}sek')
                command = str(1) + '\n'
                ser.write(command.encode())
                i = 0
                break
    i += 1
    if i > 75:
        i = 0
        command = 'r' + '\n'
        ser.write(command.encode())
        rod_delay = 1.5 + random.random()
        time.sleep(rod_delay)
        print(f'wedka{rod_delay}sek')
        command = str(1) + '\n'
        ser.write(command.encode())






