# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 22:38:47 2020

@author: 林駿騰
@description: 兩數差值
"""

def main():
    val = input("輸入值為: ").split(",")
    maxV = int("".join(sorted(val, reverse=True)))
    minV = int("".join(sorted(val)))
    print("最大值數列與最小值數量差值為 :" + str(maxV-minV))

main()