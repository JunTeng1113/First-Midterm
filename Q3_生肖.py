# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 21:40:07 2020

@author: 林駿騰
@description: 生肖
"""

def main():
    animal = ["rat", "ox", "tiger", "rabbit", "dragon", "snake", \
              "horse", "sheep", "monkey", "rooster", "dog", "pig"]
    inputYear = int(input())
    print(animal[(inputYear + 8) % 12])

main()