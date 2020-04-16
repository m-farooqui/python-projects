#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:01:52 2020

@author: mawais
"""

def brute_force(message):
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for key in range(len(LETTERS)):
        translated = []
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated.append(LETTERS[num])
            else:
                
                translated.append(symbol)
                
        print(f'key = {key}, message = {"".join(translated)}')
        
intercepted_message = "NSXYWZHYNTS KTW KNWXY QJLNTS FYYFHP YTSNLMY KWTR STWYM JFXY"
brute_force(intercepted_message)