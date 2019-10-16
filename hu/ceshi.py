#!/usr/bin/python
#-*-coding:utf-8-*-
import requests
import json
import xlrd
class Pa_chong:
    def qingqiu(self):
        a='https://sou.zhaopin.com/?jl=76…5%B7%A5%E7%A8%8B%E5%B8%88&kt=3'
        b='User-Agent:Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/69.0'
        c=requests.get(url=a,headers=b)
        d=c.content.decode('utf-8')
    def save(self):
        with open(r'E:\PycharmProjects\untitled\abc.txt','wb',encoding='utf-8')as w :
            w.write()
aa=Pa_chong()

