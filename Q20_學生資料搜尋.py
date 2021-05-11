# -*- coding: utf-8 -*-
"""
Created on 

@author: 林駿騰
@description: 學生資料搜尋
"""


def main():
    data = [["123", "Tom", "DTGD"],
            ["456", "Cat", "CSIE"],
            ["789", "Nana", "ASIE"],
            ["321", "Lim", "DBA"],
            ["654", "Won", "FDD"]]
    findindex = lambda array, i, value: sorted(array, key=lambda x: x[i] != value)[0]
    print("學生資料為: " + " ".join(findindex(data, 0, input("輸入查詢學號為: "))))
    

main()