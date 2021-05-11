# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 15:53:38 2020

@author: 林駿騰
@description: 提款機搜尋
"""

def main():
    data = [["123", "456", 9000],
            ["456", "789", 5000],
            ["789", "888", 6000],
            ["336", "558", 10000],
            ["775", "666", 12000],
            ["566", "221", 7000]]
    outlist = []
    for n in range(int(input("輸入查詢組數 N 為: "))):
        findindex = lambda array, value: sorted(array, key=lambda x: x[0] != value[0])[0][2] if sorted(array, key=lambda x: x[0] != value[0])[0][0] == value[0] and sorted(array, key=lambda x: x[0] != value[0])[0][1] == value[1] else "error"
        outlist.append(findindex(data, input().split()))
        
    for i in outlist: print(i)
main()