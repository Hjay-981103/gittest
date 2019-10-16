#!/usr/bin/python
#-*-coding:utf-8-*-
# import pymysql  #用来连接与操作数据库
# conn=pymysql.connect(host='192.168.2.138',port=3306
#                      ,user='root',passwd='123456'
#                      ,db='pachong',
#                      charset='utf-8')#连接数据库,host是ip地址,potr端口号
#                         # user用户,db数据库名,charset是数据库统一编码
# #游标
# cusor=conn.cursor()
# #执行sql语句
# cusor.execute('create table biaoming(name char);')
# cusor.execute('show tables;')
# print(cusor.fetchall())#获取上一句sql语句执行结果
# cusor.execute('show tables;')
# print(cusor.fetchmany())#默认只显示结果的第一个
# conn.commit()#提交数据
# conn.close()#断开连接
# a=int(input('请输入你的数字'))
# if a%2==0 or a%3==0:
#     if a%2==0:
#        print('hello')
#     elif a%3==0:
#         print('world')
# else:
#     print('123')
# a=str(input('请输入你的字符串'))
# b = 0
# for i in range(len(a)):
#   b += 1
#   if b < len(a) // 2:
#     if a[i] != a[len(a) - i - 1]:
#         print('bu是')
#     else:
#             break
#   else:
#       print('shi')
# a=[]
# for i in range(1,101):
#     for j in range(1,i):
#         if i%j==0:
#             a.append(j)
#     if sum(a)==i:
#        print(a)
#        print(i)
#while循环1到100的和
# a=0
# b=0
# while a<100:
#     a+=1
#     b+=a
#     print(b)
#必须参数
# def qwe(x):
#     print(x)
# qwe(13)
#默认参数
# def qwe(x):
#     print(x)
# qwe(123,345)
#可变长参数
# def qwe(*args):#*args:默认的可变长参数
#     print(args)
# qwe(12,124,32,123,543)#传入结果为元组
# def qwe(**kwargs):#**kwargs：默认的可变长参数
#     print(kwargs)
# qwe(name=123,sex='men')#传入结果为键值对的字典格式
# def qwe(x):
#     b=0
#     for i in range(x+1):
#         b+=i
#     return b,100,200
# print(qwe(10))
# def ji(x): #求鸡的数量
#     for i in range(x):
#         for j in range(x-i):
#             a=x-i-j
#             if(2*i)+j+(0.5*a)==x:
#              print('公鸡有{}只，母鸡有{}只，小鸡有{}只'.format(i,j,a))
# ji(100)

# for i in range(1,5):
#     for j in range(1,5):
#         for a in range(1,5):
#            if (i!=j)and(i!=a)and(j!=a):
#              print(i*100+j*10+a)
# print()
# a = input('成绩').split(',')
# b = []
# for i in a:
#     i = int(i)
#     b.append(i)
#     c = sum(b) / len(b)
# for j in b:
#     if j < c:
#         print('低于平均成绩：{}'.format(j))
# print('平均成绩：{}'.format(c))
# a=input('请输入你的数字')
# a=int(a)
# b=hex(a)
# print(b)
# def hanshu(b, *a):
#     for i in a:
#         for j in a:
#             if i+j==b:
#                 print(i,j)
# hanshu(6,1,2,3,4,5)
# def hanshu(x):
#     for i in range(1,x+1):
#         for j in range(1,x+1):
#             for a in range(1,x+1):
#                 if (i!=j)and(i!=a)and(j!=a):
#                     print(i*100+j*10+a)
# hanshu(4)
# def chengji(x):
#     c=sum(x)/len(x)
#     print('平均成绩：{}'.format(c))
#     for a in x:
#         if a<c:
#             print('低于平均成绩：{}'.format(a))
# chengji([67,89,56,78])
# def shuzi(x):
#     x=int(x)
#     a=hex(x)
#     print(a)
# shuzi(16)
# for i in range(1,1000):
#     a=[j for j in range(1,i) if i%j==0]
#     if sum(a)==i:
#         print(i)
# def shu(x):
#     for i in range(1,1000):
#         a=[j for j in range(1,i) if i%j==0]
#         if sum(a)==j:
#             print(j)
# shu(1000)
#d=[]
# import xlwt
# import xlrd
# with open ('h.txt','w',encoding='utf-8') as a:
#     a.write(('a,b,c,d'+'\n')*20)
# with open('h.txt','r',encoding='utf-8') as a :
#     xl=xlwt.Workbook(encoding='utf-8')
#     b=xl.add_sheet('123')
#     for i,s in enumerate(a.readlines()):
#         s=s.split(',')
#         for j,m in enumerate(s):
#            b.write(i,j,m)
#     xl.save('d.xls')
# with open('h.txt','r',encoding='utf-8') as a:
#    rd=xlrd.open_workbook('d.xls')
#    aa=rd.sheet_by_name('123')
#    hanshu=aa.nrows
#    for i in range(1,hanshu):
#        for k in aa.row_values(i):
#            a.write(k+',')
# with open('h.txt','r',encoding='utf-8')as a:
#     for i in a.readlines():
#         i=i.strip(',')
#         with open('h.txt','a',encoding='utf-8')as a:
#             a.write(i)
import paramiko
a=paramiko.Transport('192.168.10.56','端口号')
b=paramiko.connect(user='root',password='123456')
c=paramiko.SFTPClient.from_transport(b)
c.get('a.txt',r'E:\a.txt')
c.put('a.txt','/root/')
c.mkdir('/root/text')
c.rename('text','learn')
c.remove('learn')