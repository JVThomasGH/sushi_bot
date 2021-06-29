from PIL import Image, ImageGrab
import os
import time

"""
Tested on Edge Browser on laptop screen.
Scrolled 3 times with mouse wheel.
"""

# Globals
# ------------------
x_pad = 390
y_pad = 197

# x_pad = 368
# y_pad = 88


def screenGrabPartial():
    box = (x_pad + 1, y_pad + 1, x_pad + 640, y_pad + 480)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + "\\Images\\partial_snap__" + str(int(time.time())) + ".png", "PNG")

def screenGrabFull():
    box = ()
    im = ImageGrab.grab()
    im.save(os.getcwd() + "\\Images\\full_snap__" + str(int(time.time())) + ".png", "PNG")

def main():
    screenGrabPartial()
    # screenGrabFull()


if __name__ == "__main__":
    main()
