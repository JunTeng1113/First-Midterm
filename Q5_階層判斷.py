# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 21:46:28 2020

@author: 林駿騰
@description: 階層判斷
"""

def main():
    M = int(input("請輸入階乘值 M："))
    N = 0
    num = 1
    while num < M:
        N += 1
        num *= N
    print("超過 M 為", M,"的最小階層 N 值為：", N)

main()