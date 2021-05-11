# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 22:04:11 2020

@author: 林駿騰
@description: 硬幣及紙鈔的數量
"""

def main():
    val = int(input())
    amount = 0
    for i in [100, 50, 10, 5, 1]:
        amount += val // i
        val -= (val//i) * i
    print(amount)

main()