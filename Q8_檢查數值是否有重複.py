# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 22:55:06 2020

@author: 林駿騰
@description: 檢查數值是否有重複
"""

def main():
    n = int(input("輸入第一行正整數為: "))
    val = input("第二行中數列中的數字為:").split()
    if len(set(val)) == n: 
        print("每個數字剛好只出現1次")
    else:
        i = 1
        while True:
            for j in list(set(val)): val.remove(j)
            i += 1
            if len(val) == 1: 
                print("最大出現次數的數字為:" + val[0])
                print("出現次數為:" + str(i))
                break
            
main()


