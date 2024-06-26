import statistics

import pyautogui
import time
import cv2
import os
import math
from statistics import mean
import serial
import time
import random
import customtkinter as ctk
BUFF = 255
def orb_sim(img1, img2):
    orb = cv2.ORB_create()
    kp_a, desc_a = orb.detectAndCompute(img1, None)
    kp_b, desc_b = orb.detectAndCompute(img2, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(desc_a, desc_b)
    similar_regions = [i for i in matches if i.distance < 50]
    if len(matches) == 0:
        return 0
    return len(similar_regions) / len(matches)

i = 0

def main():
    global i
    pyautogui.screenshot(f"raw_data/screenshot{i}.png", region=(960, 330, 130, 180))
    image = cv2.imread(f'raw_data/screenshot{i}.png')
    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    os.remove(f"raw_data/screenshot{i}.png")
    # cv2.imwrite(f'raw_data/screenshot_gray{i}.jpg', image_gray)


    image_compared = cv2.imread('data/pic9.jpg')
    orb_similarity = orb_sim(image_gray, image_compared)
    # print(orb_similarity)
    results = []
    if orb_similarity > 0.4:

        for _ in range(1,10):
            image_to_compare = cv2.imread(f'data/pic{_}.jpg')
            smoke_similarity = orb_sim(image_gray, image_to_compare)
            print(smoke_similarity)
            # print(smoke_similarity)
            if smoke_similarity > 0.90:
                result = math.ceil((_+1)/2)
                print(result)
                recognition_delay = 1 + random.random()
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
                main()
    time.sleep(0.2)
    i += 1
    main()



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

main()