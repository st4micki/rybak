import pyautogui
import time
import cv2
import os
i = 3

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

while True:
      pyautogui.screenshot(f"raw_data/screenshot{i}.png", region=(960, 390, 120, 120))
      image = cv2.imread(f'raw_data/screenshot{i}.png')
      image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
      os.remove(f"raw_data/screenshot{i}.png")
      cv2.imwrite(f'raw_data/screenshot_gray{i}.jpg', image_gray)
      time.sleep(0.2)
      i += 1



