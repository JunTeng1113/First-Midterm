# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 11:58:15 2020

@author: 林駿騰
@description: 以三角形的方式呈現階乘結果
"""

def main():
    n = int(input("請輸入一個正整數(<10): "))
    for i in range(1, n+1):
        for j in range(1, i+1): print("%2d"%(i*j), end=" ")
        print()
main()


