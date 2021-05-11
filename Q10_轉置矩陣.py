# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 10:26:45 2020

@author: 林駿騰
@description: 轉置矩陣
"""

def main():
    n, m = list(map(int, input("輸入 N 及 M 為: ").split()))
    arr = list()
    for i in range(n): arr.append(input(F"輸入矩陣數值第 {i+1} 列為: ").split())
    for i in range(m): print(F"輸出矩陣數值第 {i+1} 列為: {arr[0][i]} {arr[1][i]}")

main()