# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 22:16:39 2020

@author: 林駿騰
@description: 撲克牌13點
"""

def main():
    list1 = input().split()
    dict1 = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, \
             "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}
    sum1 = 0
    for i in list1: sum1 += dict1[i]
    print(sum1)
    
main()
