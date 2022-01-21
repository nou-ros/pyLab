import pyautogui
import time

while True:
    time.sleep(3)
    pyautogui.typewrite('Hello!')
    pyautogui.press('enter')
