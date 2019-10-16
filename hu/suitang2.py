#!/usr/bin/python
#-*-coding:utf-8-*-
# import hu.suitang1
# hu.suitang1.hanshu()
# hu.suitang1.hanshu1()
# hu.suitang1.hanshu2()
# from hu.suitang1 import hanshu1
# shuitang1.hanshu()
# from hu.suitang1 import *
# hanshu()
# hanshu1()
# hanshu2()
#错误预防
# try:
#     safasfafs
# except NameError as a :
#     print(a)
#try...except...elsr语句
# try:
#     'asfsafsaf'
# except TypeError as a:
#     print(a)
# else:
#     print('nihao')
#try...finally语句  #捕获异常
# try:
#     asfa
# except NameError as a:
#     print(a)
# else:
#     print('nihao')
# finally:
#     print('最终执行')
# print('你好')
# raise TypeError('你错了')
# print(1234)
#十六进制
# a =[i for i in range(10)]+[chr(i)for i in range(97,103)]
# b = int(input('>>>'))
# f =[]
# while True:
#     d=b%16
#     b=b//16
#     f.append(a[d])
#     if b==0:
#         break
# f.reverse()
# print(f)
# a_list= [
#     ('汉堡',12),
#     ('奶茶',15),          #商品列表
#     ('炸鸡',20),
#     ('可乐',5),
#     ('鸡腿',12),
#     ('鸡翅',12)]
# b_list = []
# c = input("请输入你的金额:")  #输入金额
# if c.isdigit():
#     c = int(c)
#     while True:
#         for index,i in enumerate(a_list):
#             print(index,i)
#         d = input('请输入你要购买的商品')
#         if d.isdigit():
#          d = int(d)
#          if d < len(a_list) and d >= 0:
#            e = a_list[d]
#            if  e[1] < c:
#                b_list.append(d)
#                c -= e[1]
#
#                print("把%s加入你的购物车,你的余额为'%s'"%(d,c))
#
#            else:
#                print("你的余额只剩'%s'，请重新选择"%c)
#          else:
#              print("没有此商品，请重新选择商品！")
# else:
#     print("输入错误")
# #不用int将字符串转化为整数
# a='0123'
# a=a[::-1]
# b=0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j)==a[i]:
#             b+=j*10**i
# print(b)

