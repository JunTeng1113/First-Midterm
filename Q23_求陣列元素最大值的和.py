# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 00:23:35 2020

@author: 林駿騰
@description: 求陣列元素最大值的和
"""

def main():
    n = int(input("請輸入陣列大小:"))
    list1 = []
    for i in range(n): list1.extend(list(map(int, input().split())))
    max3 = [sorted(list1, reverse=True)[0], sorted(list1, reverse=True)[1], sorted(list1, reverse=True)[2]]
    print("最大值為:", sum(max3))
    loc3 = [F"({list1.index(max3[i])//n+1},{list1.index(max3[i])%n+1})" for i in range(3)]
    print("位置為", loc3[0], loc3[1], loc3[2])
    
main()

