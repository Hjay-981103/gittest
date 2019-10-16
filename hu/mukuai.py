#!/usr/bin/python
#-*-coding:utf-8-*-
import os
#实现python与操作系统之间的交互
# a=os.popen('ping 192,168.2.1')
#popen() 执行cmd命令
# print(a.read())
# os.chdir('c:')
#chdir 切换目录
# print(os.getcwd())
#getcwd 获取当前所在的目录
# os.mkdir('aaa')
#创建目录
# os.makedirs('eee/www/qqq')
#创建递归目录
# os.removedirs('eee/www/qqq')
#删除递归目录
# os.rmdir('aaa')
#删除空目录
# os.remove(r'E:\PycharmProjects\untitled\hu\11a.txt')
#remove 删除文件 加路径
# os.rename('day.1.py','day1.py')
#重命名 ('旧名字','新名字')
# print(os.listdir('c:'))
#获取目录下的所有文件 listdir 写哪个路径下就查看哪个路径下的文件
# a=os.path.split(r'E:\PycharmProjects\untitled\hu\a.mp4')
#将文件后缀名与路径分开
# a=os.path.splitext(r'E:\PycharmProjects\untitled\hu\a.mp4')
# print(a)
#判断是不是目录
# a=os.path.isdir(r'a.mp4')
# print(a)
#判断是不是文件
# a=os.path.isfile(r'a.mp4')
# print(a)
import os
# a=os.listdir()
# s=0
# c=0
# for i in a:
#     b=os.path.isfile(i)
#     if b==True:
#         s+=1
#     else:
#         c+=1
#         print(s,c)
# a =[i for i in os.listdir() if os.path.isfile(i)==True]
# # print(a)
# import time
# while True:
#     a=int(input('请输入你的年份'))
#     b=int(input('请输入你的月份'))
#     c=int(input('请输入你的日期'))
#     if a%400==0:
#        print('是闰年')
#     elif a%100!=0 and a%4==0:
#        print('是闰年')
#     else:
#        print('不是闰年')
# a ='0123'
# a=a[::-1]
# b=0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j)==a[i]:
#             b+=j*10**i
# print(b)
