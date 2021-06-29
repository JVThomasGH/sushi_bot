import os
from time import sleep

import autoit
import pyautogui as pag
import win32api
import win32con
from pywinauto.application import Application


def calc_auto():
    '''
    PyAutoGUI and AutoIt examples
    '''
    pag.press("winleft", _pause=True)  # will trigger left window key to open the start menutime.sleep(0.5)
    sleep(.1)
    pag.typewrite("calculator", interval=0.05)  # it will type calculator in the search.
    sleep(0.1)
    pag.press("enter")  # it will trigger the enter key to open the calculator.
    autoit.win_wait("Calculator")
    for i in range(1, 9):
        pag.press(str(i))
    pag.press("esc")

    sleep(0.5)
    sleep(3)
    autoit.win_close("Calculator")


def notepad_pywinauto():
    '''
    A pywinauto example for automating Notepad
    :return:
    '''
    app = Application().start("notepad.exe")
    sleep(.1)
    app.UntitledNotepad.menu_select("Help->About Notepad")
    sleep(.1)
    app.AboutNotepad.OK.click()
    sleep(.1)
    app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces=True)
    sleep(.1)
    app.UntitledNotepad.menu_select("File->Exit")
    sleep(.1)
    app.AboutNotepad.DontSave.click()


notepad_pywinauto()
