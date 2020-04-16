#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 22:46:21 2020

@author: mawais
"""

from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy as np
#coordinates of the replay button to stop the game
class cordinates():
    replaybutton = (360, 214)
    dinasaur = (149, 239)
    
def restartGame():
    pyautogui.click(cordinates.replaybutton)
    pyautogui.keyDown('down')
    
def press_space():
    pyautogui.keyUp('down')
    
    pyautogui.keyDown('space')
    
    time.sleep(.05)
    
    print("jump")
    time.sleep(.10)
    
    pyautogui.keyUp('space')
    
    pyautogui.keyDown('down')
    
def imageGrab():
    
    box = (cordinates.dinasaur[0]+30, cordinates.dinasaur[1],
           cordinates.dinasaur[0]+120,cordinates.dinasaur[1]+2)
    
    image = ImageGrab.grab(box)
    
    grayImage = ImageOps.grayscale(image)
    
    a = np.array(grayImage.getcolors())
    
    print(a.sum())
    return a.sum()

restartGame()
while True:
    
    
    
    
    
    if(imageGrab() != 435):
        press_space()
        
        time.sleep(0.1)
        