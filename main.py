import pyautogui
import time
pyautogui.FAILSAFE = False


while True:
    time.sleep(120)
    for i in range(10, 100):
        pyautogui.moveTo(500, i * 5)
    for i in range(0, 2):
        pyautogui.press('shift')
        # pyautogui.typewrite(' ')

