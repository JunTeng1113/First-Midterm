# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 13:33:05 2020

@author: 林駿騰
@description: 轉換3進位
"""

def main():
    i = int(input("請輸入十進位的正整數: "))
    print(i, "的三進位是", toThree(i))
    
def toThree(n):
    if n//3 > 0: return toThree(n//3) + str(n%3)
    else: return str(n)

main()