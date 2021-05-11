# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 10:09:38 2020

@author: 林駿騰
@description: 字根與子字串
"""

def main():
    str1 = input("輸入 s1 為: ")
    str2 = input("輸入 s2 為: ")
    if len(str2.replace(str1, "")) != len(str2): print("YES")
    else: print("NO")

main()