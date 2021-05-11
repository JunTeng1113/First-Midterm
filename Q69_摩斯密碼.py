# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 15:04:29 2020

@author: 林駿騰
@description: 摩斯密碼
"""

def main():
    dict1 = {"-----": "0", 
             ".----": "1", 
             "..---": "2", 
             "...--": "3", 
             "....-": "4", 
             ".....": "5", 
             "-....": "6", 
             "--...": "7", 
             "---..": "8", 
             "----.": "9"}
    val = input().split()
    s = ""
    for i in val: s += dict1[i]
    print(s)
    
main()
