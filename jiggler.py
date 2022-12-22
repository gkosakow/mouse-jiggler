import pyautogui as pag
import random
import time

while True:
    x = random.randint(960,961)
    y = random.randint(540,541)
    pag.moveTo(x,y)
    time.sleep(.2)