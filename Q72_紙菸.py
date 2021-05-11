# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 12:54:07 2020

@author: 林駿騰
@description: 紙菸
"""

def main():
    n = int(input("請輸入n: "))
    k = int(input("請輸入k: "))
    print(calc(n, k))
    
def calc(a, b, i=0):
    if a+i//b>0: return a + i//b + calc(a//b, b, i%b+a%b)
    else: return 0
main()

"""
標準輸入:
    5
    3
標準輸出:
    7
"""