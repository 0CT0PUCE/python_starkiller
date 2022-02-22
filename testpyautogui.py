from time import sleep
from pynput.keyboard import Controller
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, time, shutil, pyautogui
from tkinter import *
from selenium import webdriver
import os.path
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess,pyautogui,time,cv2,sys
import tkinter as tk
from ctypes import *
from pynput.keyboard import Controller
import random
import win32clipboard
from pprint import pprint, pformat



while 2<3:
    if 2<3 :
        for i in range(1,80):
            if 2<3:
                pyautogui.moveTo(600, 850)
                pyautogui.click(button='right')
                pyautogui.moveTo(620, 830)
                pyautogui.click()
                sleep(2)
                pyautogui.moveTo(550, 850)
                pyautogui.click(button='right')
                pyautogui.moveTo(600, 830)
                pyautogui.click()
                sleep(1)
                pyautogui.moveTo(1600,250)
                x, y = pyautogui.position()
                pix = pyautogui.pixel(x, y)
                while pix != (7, 61, 105):
                    pyautogui.move(0, 10)
                    x, y = pyautogui.position()
                    pix = pyautogui.pixel(x, y)
                    print(pix)
                pyautogui.click(button='right')
                sleep(1)
                pyautogui.move(0,168)
                sleep(1)
                pyautogui.move(-120,130)
                sleep(1)
                pyautogui.click()
                win32clipboard.OpenClipboard()
                data = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()
                print(data)
                data=pformat(data)
                print(data)
                t=webdriver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[35]/div[2]/div/div/div/div/div/div/div/div/span').get_attribute("textContent")
                print(t)
                d=sample_str[0]
                print(d)
                if d == 'A':
                    box = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                    box.click()
                    keyboard.type('test')
                    box1 = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
                    box1.click()
                    print('send')
            else:
                print("g")
    else :
        print("exception")


sleep(10000000000000)
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
print(data)
data=pformat(data)
print(data)
sleep(10)
pyautogui.moveTo(1600,250)
x, y = pyautogui.position()
pix = pyautogui.pixel(x, y)
while pix != (69, 69, 69):
    pyautogui.move(0, 10)
    x, y = pyautogui.position()
    pix = pyautogui.pixel(x, y)
    print(pix)
pyautogui.click(button='right')
sleep(1)
pyautogui.move(0,168)
sleep(1)
pyautogui.move(-120,130)
sleep(5)
pyautogui.click()
