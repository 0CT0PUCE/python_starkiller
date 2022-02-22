from time import sleep
import time, pyautogui

pyautogui.moveTo(600, 850)
pyautogui.click(button='right')
pyautogui.moveTo(620, 830)
pyautogui.click()
sleep(2)
pyautogui.moveTo(550, 850)
pyautogui.click(button='right')
pyautogui.moveTo(600, 830)
pyautogui.click()
pyautogui.moveTo(1600,250)
x, y = pyautogui.position()
pix = pyautogui.pixel(x, y)
while pix != (7, 61, 105):
    pyautogui.move(0, 10)
    x, y = pyautogui.position()
    pix = pyautogui.pixel(x, y)
    print(pix)
