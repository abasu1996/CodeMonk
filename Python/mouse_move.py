import time
from tkinter import RIGHT
import mouse
c_left = "left"
while True:
    mouse.move(780,250,absolute=True,duration=1)
    mouse.double_click(c_left)
    time.sleep(4)
    mouse.move(950, 350, absolute=True, duration=1)
    time.sleep(4)