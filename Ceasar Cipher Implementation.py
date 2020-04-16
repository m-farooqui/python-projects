#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:26:31 2020

@author: mawais
"""

def encrypt(text, shift = 3):
    upper_case_text = text.upper()
    encrypted_text = []
    
    for c in upper_case_text:
        if c == " ":
            encrypted_text.append(" ")
            continue
        x = (((ord(c) - 65) + shift) % 26) + 65
        encrypted_text.append(chr(x))
        
    return "".join(encrypted_text)

print(encrypt("abcd efgh", 1))    