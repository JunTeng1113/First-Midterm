# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 20:54:18 2021

@author: 林駿騰
@description: 借閱書籍
"""

def main():
    book = [["飢餓遊戲3", "解憂雜貨店", "怪獸與牠們的產地", "哈利波特6", "我的阿富汗摯友", "祈念之樹", "樓下的房客", "小王子"],
            ["房思琪的初戀樂園", "等一個人咖啡", "鬼滅之刃14", "神農嘗百草", "麥田捕手", "老人與海", "傲慢與偏見", "與神同行"]]
    inVal = input("請輸入欲租借的書籍：")
    if inVal in book[0]: print("在書架A的第", book[0].index(inVal)+1, "本")
    elif inVal in book[1]: print("在書架B的第", book[1].index(inVal)+1, "本")
    else: print("查無此書籍")

main()