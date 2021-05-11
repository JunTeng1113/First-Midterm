# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 22:01:38 2020

@author: 林駿騰
@description: 母音轉換
"""

def main():
    val = input("請輸入一串小寫英文：")
    for i in ["a", "e", "i", "o", "u"]: val = val.replace(i, ".")
    print(val)
    
main()
