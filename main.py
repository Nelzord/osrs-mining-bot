import pyautogui
import time
import threading
import random
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

cycles = 0
delay = 2
button = Button.left
button2 = Button.right
activatorkey = KeyCode(char= 'a')
exitingkey = KeyCode(char= 'b')


class ClickMouse(threading.Thread) :
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.cycles = cycles
        self.delay = delay
        self.button = button
        self.button2 = button2
        self.running = False
        self.program_running = True


    def start_clicking(self):
        self.running = True


    def stop_clicking(self):
        self.running = False


    def exit(self):
        self.stop_clicking()
        self.program_running = False


    def run(self):
        countingcycles = self.cycles
        while (self.program_running == True):
            while (self.running == True):
                randomx = random.randint(orelocation.x - 300, orelocation.x + 300)
                randomy = random.randint(orelocation.y - 300, orelocation.y + 300)
                pyautogui.moveTo(randomx, randomy, .2)
                pyautogui.moveTo(orelocation.x, orelocation.y, .2)
                mouse.click(self.button)
                time.sleep(1)
                pyautogui.moveTo(1479, 755, .2)
                mouse.click(self.button2)
                pyautogui.moveTo(1473, 797, .2)
                mouse.click(self.button)
                countingcycles = countingcycles + 1
                print(countingcycles)
                time.sleep(self.delay)


time.sleep(2)
mouse = Controller()
click_thread = ClickMouse(delay, button)
orelocation = pyautogui.position()
click_thread.start()


def on_press(key):
    if key == activatorkey:
        if (click_thread.running == True):
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exitingkey:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
