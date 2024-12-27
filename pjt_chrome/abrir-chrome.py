import pyautogui
import time


# abre janela windows
pyautogui.press('winleft')
pyautogui.press('enter')
time.sleep(1)

# abre chrome
pyautogui.write('chrome')
time.sleep(1)

pyautogui.press('enter')