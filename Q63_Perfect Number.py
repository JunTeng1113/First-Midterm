# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 16:12:31 2020

@author: 林駿騰
@description: Perfect Number
"""

def main():
    n = int(input("請輸入正整數n: "))
    i = 1
    facter = list()
    while n > i:
        if n % i == 0: facter.append(i)
        i += 1
    if sum(facter) > n: print("abundant")
    elif sum(facter) == n: print("perfect")
    else: print("deficient")
    
main()