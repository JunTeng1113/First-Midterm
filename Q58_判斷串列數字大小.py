# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 22:07:27 2020

@author: 林駿騰
@description: 判斷串列數字大小
"""

def main():
    list1 = list()
    for i in range(10):
        list1.append(int(input(F"請輸入第 {i+1} 個數字：")))
    print("最大的 3 個數字為：" + ",".join(list(map(str, reversed(sorted(list1))))[:3])) #排序 > 反轉 > 取前三個 > 合併
    print("最小的 3 個數字為：" + ",".join(list(map(str, sorted(list1)))[:3])) #排序 > 取前三個 > 合併
   
main()