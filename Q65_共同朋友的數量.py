# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 15:45:23 2020

@author: 林駿騰
@description: 共同朋友的數量
"""

def main():
    friends_a = set(input("請輸入 A 的好友: ").split())
    friends_b = set(input("請輸入 B 的好友: ").split())
    print(len(friends_a & friends_b))
    
main()
