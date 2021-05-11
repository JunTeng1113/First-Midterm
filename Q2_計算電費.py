# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 21:33:32 2020

@author: 林駿騰
@description: 計算電費
"""

def main():
    powerAmount = int(input())
    summer_fee = 0
    non_summer_fee = 0
    power      = [700 , 500 , 330 , 120 , 0]
    summer     = [5.63, 4.97, 4.39, 3.02, 2.10]
    non_summer = [4.50, 4.01, 3.61, 2.68, 2.10]
    for i in range(5):
        if powerAmount > power[i]:
            temp = powerAmount - power[i]
            powerAmount = power[i]
            summer_fee += temp * summer[i]
            non_summer_fee += temp * non_summer[i]
            
    print("Summer months:", summer_fee)
    print("Non-Summer months:", non_summer_fee)
    
main()

"""
powerAmount = int(input())
summer_fee = 0
non_summer_fee = 0
if powerAmount > 700: #701 ~
    temp = powerAmount - 700
    powerAmount = 700
    summer_fee += temp * 5.63
    non_summer_fee += temp * 4.50
    
if powerAmount > 500: #501 ~ 700
    temp = powerAmount - 500
    powerAmount = 500
    summer_fee += temp * 4.97
    non_summer_fee += temp * 4.01
    
if powerAmount > 330: #331 ~ 500
    temp = powerAmount - 330
    powerAmount = 330
    summer_fee += temp * 4.39
    non_summer_fee += temp * 3.61
    
if powerAmount > 120: #121 ~ 330
    temp = powerAmount - 120
    powerAmount = 120
    summer_fee += temp * 3.02
    non_summer_fee += temp * 2.68
    
if powerAmount > 0: # 1 ~ 120
    temp = powerAmount - 0
    powerAmount = 0
    summer_fee += temp * 2.10
    non_summer_fee += temp * 2.10
print("Summer months:", summer_fee)
print("Non-Summer months:", non_summer_fee)
"""