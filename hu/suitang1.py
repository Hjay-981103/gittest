#!/usr/bin/python
#-*-coding:utf-8-*-
#以文件名查看文件
# txt = open('223.txt',mode='r',encoding='ansi')
# a = txt.read()
# print(a)
# 以路径方式查看文件
# txt = open(r'E:\PycharmProjects\untitled\123.txt',mode='r',encoding='ansi')
# a = txt.read()
# print(a)
# 新建文件插入内容
# txt = open(r'E:\PycharmProjects\untitled\223.txt',mode='w',encoding='ansi')
# a = txt.write('如此厚颜无耻之人')
# a = txt.close()
#练习1  输入100遍你好
# txt = open(r'E:\PycharmProjects\untitled\323.txt',mode='w',encoding='ansi')
# txt.write(('\n'+'你好')*100)
# txt.close()
# #练习二  九九乘法表
# txt = open(r'333.txt','w',encoding='ansi')
# for i in range(1,10):
#    for j in range(1,i+1):
#      txt.write('{}*{}={}'.format(j,i,i*j))
#    txt.write('\n')
# txt.close()
#read.()下面可以跟任何函数
# a = open('323.txt','r',encoding='ansi')
# b = a.read()
# c = b.endswith('好')
# print(c)
#去除空格
# a = open('333.txt','r',encoding='ansi')
# b = a.readlines()
#
# for i in b:
#     c=i.rstrip('\n')
#     a=c.split(" ")
#     print(a)
# 读取：一行一行的读（具有迭代功能）
# a = open('333.txt','r',encoding='ansi')
# j = a.readline()
# h = a.readline()
# b = a.readline()
# print(j,h,b)
#先读后写
# a = open('333.txt','r+',encoding='ansi')
# b = a.read()
# c = a.write('nihao')
# print(c)
#with 语句
# with open('333.txt','r',encoding='ansi') as a:
#     print(a.read())
# def hanshu():
#     pass
# def hanshu1():
#     pass
# def hanshu2():
#     pass
# if __name__ == '__main__':
#     print('ture')
# import xlwt
# a=xlwt.Workbook(encoding='utf-8')
# b=a.add_sheet('qwe')
# with open('22.txt','r',encoding='utf-8')as w:
#     c=w.readline()
# for i in range len(a):
#    b.write(i,0,c[i])
# a.save('c.xls')
# from hu.pachong2 import jiujiu
# jiujiu()
import paramiko
a=paramiko.SFTPClient()
a.set_missing_host_key_policy(paramiko.AutoAddPolicy)
a.connect(hostname='',
          port='',
          user='',
          password='')
stuin,stuout,stuerr=a.exec_command('')
aa=stuout.read().decode('utf-8')
print(a)
a=paramiko.transport('ip地址','端口号')
a.connect(username='用户名',password='密码')
b=paramiko.SFTPClient.from_transport(a)
b.get()
b.put()
b.mkdir()
b.rename()
b.remove()
b.close()
