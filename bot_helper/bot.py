import os
import time
from time import sleep

import autoit
import pyautogui
import pyautogui as pag
import pytesseract
import win32api
import win32con
from numpy import *
import cv2
from PIL import ImageOps, ImageGrab

from pywinauto.application import Application


def get_image_size(image_path):
    img = cv2.imread(image_path)
    height, width, channels = img.shape
    return height, width


def switch_to_window(window_name):
    autoit.win_activate(window_name)


def click_image(image_path):
    wait_for_image(image_path)
    image = pag.locateCenterOnScreen(image_path, confidence=.08)
    pag.click(image)


def reset_screen(browser="firefox"):
    if browser == "firefox":
        sleep(2)
        for i in range(5):
            l_click(1910, 107)
        for i in range(5):
            l_click(1910, 1039)
        sleep(2)
    elif browser == "chrome":
        sleep(2)
        for i in range(5):
            l_click(1910, 107)
        for i in range(5):
            l_click(1910, 1039)
        sleep(2)


def get_image_loc(pic_path):
    pic = pag.locateOnScreen(pic_path, confidence=0.5)
    print("Image location: " + str(pic))
    return pic


def get_mouse_cords():
    for i in range(1):
        print(win32api.GetCursorPos())
        sleep(.5)


def l_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def r_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)


def grab_region(image_name, x1, y1, x2, y2):
    pag.screenshot(os.getcwd() + os.path.join("/Needles/" + os.path.join(image_name) + ".png"), region=(x1, y1, x2, y2))
    return os.getcwd() + os.path.join("/Needles/" + os.path.join(image_name) + ".png")


def wait_for_image(image_path):
    image = pag.locateOnScreen(image_path, confidence=0.8)
    while image == None:
        print("Waiting for Image: " + image_path)
        sleep(3)
    return image


def move_to_image(x, y, s=0.0):
    pag.moveTo(x, y, s)


def screen_size():
    print(pag.size())


def countdownTimer(secs):
    print("Starting", end="")
    pass
    for i in range(0, secs):
        print(".", end="")
        sleep(1)
    print("Go!")


def image_path(pic):
    '''
    Provide image file name without the png extension.\n
    Combine it with the game folder name.\n
    example: Diski/image\n
    :param pic:
    :return:
    '''
    # os.chdir("..")
    script_dir = os.getcwd()
    image_path = os.path.join(
        script_dir,
        "Needles",
        pic + ".png"
    )
    return image_path


def grab_gray():
    print("Grabbing Gray Image Section... ")
    sleep(1)
    box = (356, 111, 1540, 1011)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    im.save(os.getcwd() + "/Images/full_snap_gray__" + str(int(time.time())) + ".png", "PNG")
    print(a)
    return a


def get_ocr(image_path):
    pytesseract.pytesseract.tesseract_cmd = r'C:/Users/JodyT/AppData/Local/Programs/Tesseract-OCR/tesseract'
    return pytesseract.image_to_string(image_path)
