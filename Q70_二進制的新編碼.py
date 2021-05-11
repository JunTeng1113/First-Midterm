# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:28:06 2020

@author: 林駿騰
@description: 二進制的新編碼
"""

def main():
    dict1 = {"00": "0", 
             "01": "1", 
             "100": "2", 
             "101": "3", 
             "1100": "4", 
             "1101": "5", 
             "11100": "6", 
             "11101": "7", 
             "111100": "8", 
             "111101": "9"}
    eng = "DEFGHIJKLMNOPQRSTUVWXYZABC"
    val = input().split()
    s = ""
    for i in val: s += dict1[i]
    print(eng[int(s)-1])
    
main()
