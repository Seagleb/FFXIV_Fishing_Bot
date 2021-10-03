from PIL import ImageGrab, Image
import pyautogui
import time


def cast():
    print('Casting...')
    pyautogui.mouseDown(x=854, y=912, button='left')
    time.sleep(.10)
    pyautogui.mouseUp(x=854, y=912, button='left')


def hook():
    time.sleep(1)
    print('Hooking...')
    pyautogui.mouseDown(x=890, y=912, button='left')
    time.sleep(.10)
    pyautogui.mouseUp(x=890, y=912, button='left')


def wait_for_bite():
    while True:
        image = ImageGrab.grab()
        is_green = False
        for y in range(410, 610):
            for x in range(880, 1050):
                color = image.getpixel((x, y))
                if (color[0] >= 100 and color[0] <= 270 and color[1] >= 130 and color[2] <= 70):
                    is_green = True
        if is_green == False:
            print('BITE!!!')
            hook()
            return True


def fish():
    time.sleep(2)
    cast()
    time.sleep(5)
    wait_for_bite()
    time.sleep(8)
    fish()

fish()
# pyautogui.FAILSAFE = False
# screenWidth, screenHeight = pyautogui.size()
# 
# pyautogui.moveTo(800, 800, duration = 1)
# pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
