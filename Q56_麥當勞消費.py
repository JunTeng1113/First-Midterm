# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 09:38:03 2020

@author: 林駿騰
@description: 麥當勞消費
"""

def main():
    meal1 = {"1": 72, "2": 62, "3": 82, "4": 44, "5": 60}
    mealA = {"A": 55, "B": 68}
    drink = {"是": 7, "否": 0}
    fries = {"是": 13, "否": 0}
    money = 0
    meal = list(input("請選擇主餐及升級的套餐："))
    money += meal1[meal[0]]
    money += mealA[meal[1]]
    money += drink[input("是否升級成大杯飲料：")]
    money += fries[input("是否換成大薯：")]
    print(f"總共為 {money} 元")
    
main()
