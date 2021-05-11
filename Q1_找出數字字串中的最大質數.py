# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 21:50:34 2020

@author: 林駿騰
@description: 找出數字字串中的最大質數
"""

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0: return False
    return True

def main():
    s = input("請輸入正整數 :")
    m = 0
    for i in range(len(s)):
        for j in range(len(s)-i):
            t = int(s[i:i+j+1])
            if isPrime(t) and t > m:
                m = t
    if m == 0: m = "No prime found"
    print("子字串中最大的質數值為 :" + str(m))

main()