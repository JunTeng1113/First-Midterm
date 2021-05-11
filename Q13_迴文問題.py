# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 22:02:05 2020

@author: 林駿騰
@description: 迴文問題
"""

def main():
    str1 = input("輸入一字元為: ")
    if str1 == str1[::-1]: print("YES")
    else: print("NO")
    
main()