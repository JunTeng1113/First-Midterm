# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 15:50:11 2020

@author: 林駿騰
@description: 孿生質數
"""

def main():
    number1 = int(input("請輸入第一個要判斷的數字: "))
    number2 = int(input("請輸入第二個要判斷的數字: "))
    check = lambda a, b: "Y" if isPrime(a) and isPrime(b) else "N"
    print(check(number1, number2))
    
def isPrime(n):
    for i in [2] + list(range(3, int(n**0.5)+1, 2)):
        if n%i == 0: return False
    return True

main()