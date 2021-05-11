# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 10:03:56 2020

@author: 林駿騰
@description: 迴圈練習
"""

def main():
    n = int(input())
    for i in range(1, n+1): print(" "*abs((n+1)//2-i) + "*"*(n-abs((n+1)//2-i)*2) + " "*abs((n+1)//2-i))

main()