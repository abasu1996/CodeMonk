import pyautogui as pt
from time import sleep
for i in range(6):

# while True:
    posXY = pt.position()
    print(posXY, pt.position(posXY[0],posXY[1]), pt.pixel(posXY[0],posXY[1]))
    sleep(2)
    if posXY == 0:
        break
