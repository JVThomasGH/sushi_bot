import pyautogui
import win32process
from PIL import Image, ImageGrab, ImageOps
import os
import keyboard
import time
import win32api, win32con
from selenium import webdriver
import os
import glob
import PIL.ImageOps
from numpy import *
from Cord import Cord
from blank import Blank
import operator
import pytesseract

# Globals
# ------------------
x_pad = 390
y_pad = 197

sushiTypes = {1910: 'onigiri',
              2555: 'caliroll',
              1916: 'gunkan',
              1884: 'salmon_roll',
              2333: 'shrimp_sushi',
              2134: 'unagi_roll',
              2549: 'dragon_roll',
              3929: 'combi_sushi'}

foodOnHand = {'shrimp': 5,
              'rice': 10,
              'nori': 10,
              'roe': 10,
              'salmon': 5,
              'unagi': 5}


def main():
    # buyFood("rice")
    # check_you_win()
    # check_shrimp_level()
    # screenGrabGoal()
    # get_ocr_text()

    launch_page()
    startGame()
    for i in range(500):
        run_game()
        check_fail()
        fail_continue_watermark()
        fail_try_again()
        check_you_win()
        check_today_goal()
        print("Round: " + str(i))

    # get_seat_one()q
    # get_seat_two()
    # get_seat_three()
    # get_seat_four()
    # get_seat_five()
    # get_seat_six()


def countdownTimer(secs):
    # Countdown Timer
    print("Starting", end="")
    for i in range(0, secs):
        print(".", end="")
        time.sleep(1)
    print("Go!")


def launch_page():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.miniclip.com/games/sushi-go-round")
    time.sleep(5)
    driver.execute_script("arguments[0].scrollIntoView();",
                          driver.find_element_by_css_selector("section#game-container > .game-embed-wrapper"))

    time.sleep(10)


def screenGrabHere():
    box = (x_pad + 1, y_pad + 1, x_pad + 640, y_pad + 480)
    im = ImageGrab.grab(box)
    # im.save(os.getcwd() + "\\Images\\full_snap__" + str(int(time.time())) + ".png", "PNG")
    return im


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print("Click Left")  # completely optional. But nice for debugging purposes.


def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    print("Left Down")


def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    print("Left Release")


def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))


def sound_off():
    # Location of SOUND button
    mousePos((326, 370))
    leftClick()
    time.sleep(.1)


def startGame():
    # Location of PLAY button
    mousePos(Cord.start_play_button)
    leftClick()
    time.sleep(.3)

    # Location of CONTINUE iPhone button
    mousePos(Cord.start_continue_iphone_button)
    leftClick()
    time.sleep(.3)

    # Location of CONTINUE button 2
    mousePos(Cord.start_continue_2_button)
    leftClick()
    time.sleep(.3)

    # Location of SKIP button
    mousePos(Cord.start_skip_tutorial_button)
    leftClick()
    time.sleep(.3)

    # Location of TODAY'S GOAL CONTINUE button
    mousePos(Cord.start_today_goal_button)
    leftClick()
    time.sleep(.3)


def clear_tables():
    print("Clearing Table 1")
    mousePos(Cord.e_plate_1)
    leftClick()

    print("Clearing Table 2")
    mousePos(Cord.e_plate_2)
    leftClick()

    print("Clearing Table 3")
    mousePos(Cord.e_plate_3)
    leftClick()

    print("Clearing Table 4")
    mousePos(Cord.e_plate_4)
    leftClick()

    print("Clearing Table 5")
    mousePos(Cord.e_plate_5)
    leftClick()

    print("Clearing Table 6")
    mousePos(Cord.e_plate_6)
    leftClick()
    time.sleep(1)


def foldMat():
    print("Folding the mat...")
    mousePos(Cord.fold_mat)
    leftClick()
    time.sleep(.1)


def makeFood(food):
    if food == 'caliroll':
        print('Making a caliroll')
        print(foodOnHand.items())
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        print(foodOnHand.items())
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        foldMat()
        time.sleep(1.5)
    elif food == 'onigiri':
        print('Making a onigiri')
        print(foodOnHand.items())
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        print(foodOnHand.items())
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        foldMat()
        time.sleep(1.5)
    elif food == 'gunkan':
        print('Making a gunkan')
        print(foodOnHand.items())
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2
        print(foodOnHand.items())
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        foldMat()
        leftClick()
        time.sleep(1.5)
    elif food == 'salmon_roll':
        print('Making a salmon roll')
        print(foodOnHand.items())
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['salmon'] -= 2
        print(foodOnHand.items())
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_salmon)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_salmon)
        leftClick()
        foldMat()
        leftClick()
        time.sleep(1.5)
    elif food == 'shrimp_sushi':
        print('Making a salmon roll')
        print(foodOnHand.items())
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['shrimp'] -= 2
        print(foodOnHand.items())
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_shrimp)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_shrimp)
        leftClick()
        foldMat()
        leftClick()
        time.sleep(1.5)
    elif food == 'unagi_roll':
        print('Making a an Unagi Roll')
        print(foodOnHand.items())
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['unagi'] -= 2
        print(foodOnHand.items())
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_unagi)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_unagi)
        leftClick()
        foldMat()
        leftClick()
        time.sleep(1.5)
    elif food == 'dragon_roll':
        print('Making a an Dragon Roll')
        print(foodOnHand.items())
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        foodOnHand['unagi'] -= 2
        print(foodOnHand.items())
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_unagi)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_unagi)
        leftClick()
        foldMat()
        leftClick()
        time.sleep(1.5)
    elif food == 'combi_sushi':
        print('Making a an Dragon Roll')
        print(foodOnHand.items())
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        foodOnHand['salmon'] -= 1
        foodOnHand['unagi'] -= 1
        foodOnHand['shrimp'] -= 1
        print(foodOnHand.items())
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_salmon)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_unagi)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_shrimp)
        leftClick()
        foldMat()
        leftClick()
        time.sleep(1.5)


def buyFood(food):
    if food == 'rice':
        # Click on phone
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()

        # Click on Topping
        time.sleep(.1)
        mousePos(Cord.menu_rice)
        time.sleep(.05)
        leftClick()
        time.sleep(.1)

        s = screenGrabHere()
        print("Order Rice:")
        print(s.getpixel(Cord.buy_rice))

        if s.getpixel(Cord.buy_rice) != (127, 127, 127):
            time.sleep(.1)
            print('Rice is available')
            mousePos(Cord.buy_rice)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice'] += 10
            print("Bought 10 Rice")
            print(foodOnHand.items())
            time.sleep(.1)
            leftClick()
        else:
            print('Rice is NOT available')
            mousePos(Cord.toppings_end_call)
            leftClick()
            time.sleep(2)
            # buyFood(food)

    if food == 'nori':
        # Click on phone
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()

        # Click on Topping
        time.sleep(.1)
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        time.sleep(.1)

        s = screenGrabHere()
        print("Toppings Blocks:")
        print(s.getpixel(Cord.toppings_nori))
        mousePos(Cord.toppings_nori)

        if s.getpixel(Cord.toppings_nori) != (33, 30, 11):
            time.sleep(.1)
            print('Nori is available')
            mousePos(Cord.toppings_nori)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            print("Bought 10 Nori")
            print(foodOnHand.items())
            time.sleep(.1)
            leftClick()
        else:
            print('Nori is NOT available')
            mousePos(Cord.toppings_end_call)
            leftClick()
            time.sleep(2)
            # buyFood(food)

    if food == 'roe':
        # Click on phone
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()

        # Click on Topping
        time.sleep(.1)
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        time.sleep(.1)

        s = screenGrabHere()
        print("Toppings Blocks:")
        print(s.getpixel(Cord.toppings_roe))

        mousePos(Cord.toppings_roe)
        print(s.getpixel(Cord.toppings_roe))

        if s.getpixel(Cord.toppings_roe) != (127, 61, 0):
            time.sleep(.1)
            print('Roe is available')
            mousePos(Cord.toppings_roe)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['roe'] += 10
            print("Bought 10 roe")
            print(foodOnHand.items())
            time.sleep(.1)
            leftClick()
        else:
            print('Roe is NOT available')
            mousePos(Cord.toppings_end_call)
            leftClick()
            time.sleep(2)
            # buyFood(food)

    if food == 'shrimp':
        # Click on phone
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()

        # Click on Topping
        time.sleep(.1)
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        time.sleep(.1)

        s = screenGrabHere()
        print("Toppings Blocks:")
        print(s.getpixel(Cord.toppings_shrimp))

        mousePos(Cord.toppings_shrimp)
        print(s.getpixel(Cord.toppings_shrimp))

        if s.getpixel(Cord.toppings_shrimp) != (127, 52, 6):
            time.sleep(.1)
            print('Shrimp is available')
            mousePos(Cord.toppings_shrimp)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['shrimp'] += 5
            print("Bought 10 Shrimp")
            print(foodOnHand.items())
            time.sleep(.1)
            leftClick()
        else:
            print('Shrimp is NOT available')
            mousePos(Cord.toppings_end_call)
            leftClick()
            time.sleep(2)
            # buyFood(food)

    if food == 'unagi':
        # Click on phone
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()

        # Click on Topping
        time.sleep(.1)
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        time.sleep(.1)

        s = screenGrabHere()
        print("Toppings Blocks:")
        print(s.getpixel(Cord.toppings_unagi))

        mousePos(Cord.toppings_unagi)
        print(s.getpixel(Cord.toppings_unagi))

        if s.getpixel(Cord.toppings_unagi) != (94, 49, 8):
            time.sleep(.1)
            print('Unagi is available')
            mousePos(Cord.toppings_unagi)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['unagi'] += 5
            print("Bought 10 Unagi")
            print(foodOnHand.items())
            time.sleep(.1)
            leftClick()
        else:
            print('Unagi is NOT available')
            mousePos(Cord.toppings_end_call)
            leftClick()
            time.sleep(2)
            # buyFood(food)

    if food == 'salmon':
        # Click on phone
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()

        # Click on Topping
        time.sleep(.1)
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        time.sleep(.1)

        s = screenGrabHere()
        print("Toppings Blocks:")
        print(s.getpixel(Cord.toppings_salmon))

        mousePos(Cord.toppings_salmon)
        print(s.getpixel(Cord.toppings_salmon))

        if s.getpixel(Cord.toppings_salmon) != (127, 71, 47):
            time.sleep(.1)
            print('Salmon is available')
            mousePos(Cord.toppings_salmon)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['salmon'] += 5
            print("Bought 10 Salmon")
            print(foodOnHand.items())
            time.sleep(.1)
            leftClick()
        else:
            print('Salmon is NOT available')
            mousePos(Cord.toppings_end_call)
            leftClick()
            time.sleep(2)
            # buyFood(food)


def checkFoodStock():
    for i, j in foodOnHand.items():
        if i == 'nori' \
                or i == 'rice' \
                or i == 'roe' \
                or i == 'shrimp' \
                or i == 'unagi' \
                or i == 'salmon':
            if j <= 3:
                print(i + ' is low and needs to be replenished')
                buyFood(i)
            else:
                print("Food supplies are OK")


def get_seat_one():
    box = (x_pad + 27, y_pad + 60, x_pad + 23 + 63, y_pad + 60 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    # im.save(os.getcwd() + '\\Images\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_seat_two():
    box = (x_pad + 128, y_pad + 60, x_pad + 124 + 63, y_pad + 60 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    # im.save(os.getcwd() + '\\Images\\seat_two__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_seat_three():
    box = (x_pad + 229, y_pad + 60, x_pad + 225 + 63, y_pad + 60 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    # im.save(os.getcwd() + '\\Images\\seat_three__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_seat_four():
    box = (x_pad + 330, y_pad + 60, x_pad + 326 + 63, y_pad + 60 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    # im.save(os.getcwd() + '\\Images\\seat_four__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_seat_five():
    box = (x_pad + 431, y_pad + 60, x_pad + 427 + 63, y_pad + 60 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    # im.save(os.getcwd() + '\\Images\\seat_five__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_seat_six():
    box = (x_pad + 532, y_pad + 60, x_pad + 528 + 63, y_pad + 60 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    # im.save(os.getcwd() + '\\Images\\seat_six__' + str(int(time.time())) + '.png', 'PNG')
    return a


def clean_folder():
    files = glob.glob('C:\\Learning\\GameBot\\Images\\*')
    for f in files:
        os.remove(f)


def run_game():
    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        if sushiTypes.__contains__(s1):
            print('table 1 is occupied and needs %s' % sushiTypes[s1])
            makeFood(sushiTypes[s1])
        else:
            print('sushi not found!\n sushiType = %i' % s1)
    else:
        print('Table 1 unoccupied')

    # checkFoodStock()
    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if sushiTypes.__contains__(s2):
            print('table 2 is occupied and needs %s' % sushiTypes[s2])
            makeFood(sushiTypes[s2])
        else:
            print('sushi not found!\n sushiType = %i' % s2)
    else:
        print('Table 2 unoccupied')
    clear_tables()

    checkFoodStock()
    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if sushiTypes.__contains__(s3):
            print('table 3 is occupied and needs %s' % sushiTypes[s3])
            makeFood(sushiTypes[s3])
        else:
            print('sushi not found!\n sushiType = %i' % s3)

    else:
        print('Table 3 unoccupied')

    checkFoodStock()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if sushiTypes.__contains__(s4):
            print('table 4 is occupied and needs %s' % sushiTypes[s4])
            makeFood(sushiTypes[s4])
        else:
            print('sushi not found!\n sushiType = %i' % s4)

    else:
        print('Table 4 unoccupied')

    checkFoodStock()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if sushiTypes.__contains__(s5):
            print('table 5 is occupied and needs %s' % sushiTypes[s5])
            makeFood(sushiTypes[s5])
        else:
            print('sushi not found!\n sushiType = %i' % s5)

    else:
        print('Table 5 unoccupied')

    checkFoodStock()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if sushiTypes.__contains__(s6):
            print('table 6 is occupied and needs %s' % sushiTypes[s6])
            makeFood(sushiTypes[s6])
        else:
            print('sushi not found!\n sushiType = %i' % s6)

    else:
        print('Table 6 unoccupied')

    clear_tables()


def check_you_win():
    t = (1, -240)
    you_win = pyautogui.locateCenterOnScreen("C:\\Learning\\GameBot\\sushi_images\\you_win.png")
    if you_win:
        print(you_win)
        continue_button_win = tuple(map(operator.sub, you_win, t))
        pyautogui.click(continue_button_win)


def check_fail():
    fail = pyautogui.locateCenterOnScreen("C:\\Learning\\GameBot\\sushi_images\\fail.png")
    fail_continue = pyautogui.locateCenterOnScreen("C:\\Learning\\GameBot\\sushi_images\\fail_continue.png")

    if fail:
        print("❌ YOU FAILED! ❌")
        print(fail)
        pyautogui.click(fail_continue)
        print("Failed... continue")
        # time.sleep(1.5)


# def fail_continue():
#     pyautogui.click(fail_continue)
#     print("Continue Next...")
#     # time.sleep(1.5)


def fail_continue_watermark():
    fail_next = pyautogui.locateCenterOnScreen("C:\\Learning\\GameBot\\sushi_images\\fail_continue_next.png")
    pyautogui.click(fail_next)
    print("Continue Watermark")
    # time.sleep(1.5)


def fail_try_again():
    try_again_yes = pyautogui.locateCenterOnScreen("C:\\Learning\\GameBot\\sushi_images\\try_again_yes.png")
    pyautogui.click(try_again_yes)
    print("Try again...")
    # time.sleep(1.5)
    check_today_goal()


def check_today_goal():
    t = (1, -240)
    goal = pyautogui.locateCenterOnScreen("C:\\Learning\\GameBot\\sushi_images\\today_goal_header.png")
    if goal:
        print(goal)
        continue_button_win = tuple(map(operator.sub, goal, t))
        screenGrabGoal()
        get_ocr_text()
        pyautogui.click(continue_button_win)


def check_shrimp_level():
    food_item = pyautogui.locateCenterOnScreen("C:\\Learning\\GameBot\\sushi_images\\shrimp_text.png")
    if food_item:
        print(food_item)
        screenGrabGoal()
        get_ocr_text()
        print(pytesseract.image_to_string(r'C:\\Learning\\GameBot\\sushi_images\\shrimp_text.png'))


def get_ocr_text():
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\JodyT\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract'
    # print(pytesseract.image_to_string(r'C:\\Learning\\GameBot\\Images\\today_goal.png'))


def grab():
    box = (x_pad + 1, y_pad + 1, x_pad + 640, y_pad + 480)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    im.save(os.getcwd() + "\\Images\\full_snap_gray__" + str(int(time.time())) + ".png", "PNG")
    print(a)
    return a


def screenGrabGoal():
    x, y = 530, 288
    box = (x, y, x + 360, y + 262)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + "\\Images\\today_goal" + ".png", "PNG")


check_you_win()

if __name__ == "__main__":
    main()
