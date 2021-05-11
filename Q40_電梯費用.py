# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 11:03:24 2020

@author: 林駿騰
@description: 電梯費用
"""

def main():
    n = int(input("搭了幾次電梯: "))
    start = 1
    sum1 = 0
    for i in range(n):
        inVal = int(input())
        sum1 += elevator(start, inVal)
        start = inVal
    print(sum1, "元")
    
def elevator(start, end):
    return cmp(end - start) * 20 + cmp(start - end) * 10
    
def cmp(n):
    return n * int(n > 0)

main()

