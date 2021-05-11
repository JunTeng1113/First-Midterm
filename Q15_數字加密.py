# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 22:06:47 2020

@author: 林駿騰
@description: 數字加密
"""

def main():
    list1 = list(input("輸入一組四位數字為: "))
    for i in range(4): list1[i] = str((int(list1[i])+7)%10)
    list1[0], list1[2] = list1[2], list1[0]
    list1[1], list1[3] = list1[3], list1[1]
    print("".join(list1))
    
main()