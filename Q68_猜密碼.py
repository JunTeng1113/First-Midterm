# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 15:09:09 2020

@author: 林駿騰
@description: 猜密碼
"""

def main():
    ans = list(map(int, list(input("請輸入第一組數字: ")))) #輸入答案, 分割儲存成list
    val = list(map(int, list(input("請輸入第二組數字: ")))) #輸入密碼, 分割儲存成list
    a, b = 0, 0
    for i in range(len(val)): 
        if val[i] == ans[i]: a += 1 #位置相同, 數字相同 A+1
        elif val[i] in ans: b += 1 #位置不同, 但數字相同 B+1
    if a == len(val): print(F"{a}A{b}B 全對")
    else: print(F"{a}A{b}B 加油")
    
main()