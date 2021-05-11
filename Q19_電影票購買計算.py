# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 00:14:09 2020

@author: 林駿騰
@description: 電影票購買計算
"""

def main():
    n = int(input("組數為:"))
    outlist = list()
    for i in range(n):
        inv = list(map(int, input(F"第 {i+1} 組:").split()))
        outlist.append(250 * inv[0] + 175 * inv[1])
    for i in range(n):
        print(F"第 {i+1} 組應收費用:", outlist[i])
        
main()


