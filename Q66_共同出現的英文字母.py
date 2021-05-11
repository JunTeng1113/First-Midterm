# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 15:31:45 2020

@author: 林駿騰
@description: 共同出現的英文字母
"""

def main():
    string_a = set(input("請輸入string_a: "))
    string_b = set(input("請輸入string_b: "))
    s = lambda a, b: "".join(a & b) if a & b else "N"
    print("".join(sorted(s(string_a, string_b))))
    
main()


