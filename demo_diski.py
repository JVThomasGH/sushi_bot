# import os
import random
from time import sleep

import cv2
import pyautogui
import pyautogui as pag
from numpy import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from image_objects import ImagesObjects as iOB

from bot_helper import bot

base_url = "https://qa.nationallottery.co.za/"
userid = "0823914052"
passw = "12345"
screen_size = ("1920", "1080")

driver = webdriver.Firefox()


def main():
    play_random_loop(3)
    # click_play_button()
    # play_sequence_loop(1)
    # check_information_table()


def play_random_loop(n):
    launch_page()
    login_to_site(userid, passw)
    nav_to_play_now_eaziwin()
    open_diski_action()
    bot.switch_to_window("ITHUBA National Lottery Play Eaziwin")
    sleep(5)
    bot.reset_screen("firefox")
    sound_pop_up_diski("off")
    click_play_button()

    for i in range(n):
        take_shots_random()
        get_red_banner()
        get_play_again_button()
        bot.reset_screen("firefox")


def play_sequence_loop(n):
    launch_page()
    login_to_site(userid, passw)

    nav_to_play_now_eaziwin()
    open_diski_action()
    bot.switch_to_window("ITHUBA National Lottery Play Eaziwin")
    bot.reset_screen("firefox")
    sound_pop_up_diski("off")
    click_play_button()
    get_red_banner()

    for i in range(n):
        take_shots()
        get_red_banner()
        get_play_again_button()
        bot.reset_screen("firefox")


def check_information_table():
    # launch_page()
    # login_to_site(userid, passw)
    # nav_to_play_now_eaziwin()

    # open_diski_action()
    bot.switch_to_window("ITHUBA National Lottery Play Eaziwin")
    bot.reset_screen("firefox")
    # sound_pop_up_diski("off")
    # click_play_button()
    # get_play_again_button()
    # click_info_icon()
    # click_info_right_arrow()
    # click_info_left_arrow()
    click_info_back_to_game()


def launch_page():
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(base_url)


def login_to_site(userid, passw):
    driver.find_element(By.CSS_SELECTOR, ".basicLoginWrap [name='userName_email']").send_keys(userid)
    driver.find_element(By.CSS_SELECTOR, ".basicLoginWrap [name='password']").send_keys(passw)
    driver.find_element(By.CSS_SELECTOR, ".btnDefault").click()


def nav_to_play_now_eaziwin():
    sleep(5)
    actions = ActionChains(driver)
    play_now_link = driver.find_element(By.CSS_SELECTOR, ".sp-megamenu-parent > :nth-child(2) > .playNowLink")
    actions \
        .move_to_element(play_now_link) \
        .pause(.9) \
        .move_to_element(driver.find_element(By.CSS_SELECTOR, ".sp-menu-center")) \
        .click(driver.find_element(By.CSS_SELECTOR,
                                   ".sp-menu-center > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(6) > a:nth-child(1) > span:nth-child(2)")) \
        .perform()


def open_diski_action():
    print("Playing Diski Action")
    element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@onclick,'playGame(\"Diski-Action\", \"0\", \"fg_0\", this);')]")))
    driver.execute_script("arguments[0].scrollIntoView();", element)
    sleep(1)
    element.click()
    driver.execute_script("arguments[0].click();", element)


def sound_pop_up_diski(sound="off"):
    '''
    Turn Game sound On or Off at startup \n
    :param sound: off / on
    :return:
    '''
    sleep(10)
    bot.reset_screen("firefox")
    img_box = bot.wait_for_image(iOB.diski_sound_pop_up)
    if sound == "off":
        no_btn_diski_sound = (img_box[0] + 127, img_box[1] + 189)
        (x, y) = no_btn_diski_sound
        bot.l_click(x, y)
    elif sound == "on":
        yes_btn_diski_sound = (img_box[0] + 284, img_box[1] + 191)
        (x, y) = yes_btn_diski_sound
        bot.l_click(x, y)


def click_play_button():
    print("Clicking Play Button")
    pag.click(iOB.diski_play_now_button)


def take_shots_random():
    sleep(4)
    # img = bot.grab_region("main_diski_play", 357, 109 ,1185, 898 )
    kicks = pag.locateOnScreen(iOB.diski_main_window_shoot, confidence=0.8)
    left_kick = kicks[0] + 423, kicks[1] + 579
    top_left_kick = kicks[0] + 449, kicks[1] + 443
    top_kick = kicks[0] + 596, kicks[1] + 406
    top_right_kick = kicks[0] + 731, kicks[1] + 444
    right_kick = kicks[0] + 762, kicks[1] + 557

    shuffle_kicks = [left_kick, top_left_kick, top_kick, top_right_kick, right_kick, right_kick]
    random.shuffle(shuffle_kicks)

    for i in range(6):
        pag.click(shuffle_kicks[i])
        sleep(3)


def take_shots():
    sleep(4)
    # img = bot.grab_region("main_diski_play", 357, 109 ,1185, 898 )
    kicks = pag.locateOnScreen(iOB.diski_main_window_shoot, confidence=0.8)
    left_kick = kicks[0] + 423, kicks[1] + 579
    top_left_kick = kicks[0] + 449, kicks[1] + 443
    top_kick = kicks[0] + 596, kicks[1] + 406
    top_right_kick = kicks[0] + 731, kicks[1] + 444
    right_kick = kicks[0] + 762, kicks[1] + 557

    pag.click(left_kick)
    sleep(3)
    pag.click(top_left_kick)
    sleep(3)
    pag.click(top_kick)
    sleep(3)
    pag.click(top_right_kick)
    sleep(3)
    pag.click(right_kick)
    sleep(4)
    pag.click(top_kick)
    sleep(3)


def get_red_banner():
    bot.reset_screen("firefox")
    try:
        sleep(2)
        points = pag.locateOnScreen(iOB.diski_main_window_shoot, confidence=0.8)
        x, y = points[0] + 7, points[1]
        img = bot.grab_region("red_banner", x + 7, y + 689, 1179, 39)
        sleep(1)
        print(bot.get_ocr(img))
    except IOError:
        print("Unable to capture red banner image")


def get_play_again_button():
    pag.click(iOB.diski_play_again)


def click_info_icon():
    img_path = bot.image_path(iOB.common_info_icon)
    pag.click(img_path)
    print(bot.get_ocr(img_path))


def click_info_back_to_game():
    sleep(1)
    print(pag.locateCenterOnScreen(iOB.diski_info_table_1_text))
    pag.moveTo(iOB.diski_info_table_1_text)
    # print(pag.locateOnScreen("C:/Learning/GameBot/Needles/Diski/main_diski_play.png"))
    # bot.grab_region("diski_info_1", 1, 2, 3, 4)
    # img = bot.image_path("Diski/back_to_game_diski")
    # bot.wait_for_image(img)
    # pag.click(img)


def click_info_right_arrow():
    sleep(1)
    img = bot.image_path(iOB.diski_back_to_game_right_arrow)
    bot.wait_for_image(img)
    pag.click(img)


def click_info_left_arrow():
    sleep(1)
    img = bot.image_path(iOB.diski_back_to_game_left_arrow)
    bot.wait_for_image(img)
    pag.click(img)


def get_image_path(pic_name):
    script_dir = os.path.dirname(__file__)
    needle_path = os.path.join(
        script_dir,
        "Needles",
        pic_name
    )
    print(needle_path)
    return needle_path


if __name__ == "__main__":
    main()
