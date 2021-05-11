# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 15:18:50 2020

@author: 林駿騰
@description: 最大公因數
"""

import math

def main():
    val = list(map(int, input("輸入值為: ").split(",")))
    print(gcd_list(val))
        
def gcd_list(array):
    max_val = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if math.gcd(array[i], array[j]) > max_val: 
                max_val = math.gcd(array[i], array[j])
    return max_val

main()