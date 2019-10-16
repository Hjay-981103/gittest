#!/usr/bin/python
#-*-coding:utf-8-*-
# import xlwt  #导入xlwt模块，只有写入的权限
# xl=xlwt.Workbook(encoding='utf-8')  #设置excel文件的格式
# sheet=xl.add_sheet('python_test')  #添加一个标签页（标签页的名称可以修改）
# sheet.write(0,0,'内容')  #向标签页里写入内容，第一个代表行  第二个代表列
# #第三个写入的是内容
# sheet.write(1,0,)
# xl.save('a.xls')
# import xlwt
# a = 0
# txt = open(r'E:\PycharmProjects\untitled\345.txt',mode='w',encoding='ansi')
# txt.write(('\n'+'你好')*100)
# txt.close()
# xl=xlwt.Workbook(encoding='utf-8')
# sheet=xl.add_sheet('new')
# sheet.write(a,a+1,txt)
# xl.save('b.xls')
# import xlrd
# #
# xl=xlrd.open_workbook('a.xls') #打开我们要操作的excel文件，括号里是文件名或者路径
# a=xl.nsheets  #1.通过索引来进入操作的标签页
# print(a)
# sheet=xl.sheets()[0]#通过索引来进入操作的标签页
# hanshu=sheet.nrows #获取标签页中有多少行
# print(hanshu)

# name=xl.sheet_names()            #2.通过名称来进入操作的标签页
# print(name)
# sheet=xl.sheet_by_name('python_test')#通过标签页的名称进入要操作的标签页
# hanshu=sheet.nrows  #获取标签页中有多少行
# print(hanshu)
# hang1=sheet.row_values(1)
# print(hang1)
# lieshu=sheet.ncols#获取标签页中有多少列
# print(lieshu)
# lie0=sheet.col_values(0)#获取标签页中的第几列
# print(lie0)
# gezi=sheet.cell(0,0).value#获取一个格子里的内容
# print(gezi)
# import xlwt      #九九乘法表写入Excel中
# xl=xlwt.Workbook(encoding='utf-8')
# sheet=xl.add_sheet('python_test')
# for i in range(1,10):
#     for j in range(1,i+1):
#         sheet.write(i,j,f'{i}*{j}={i*j}')
# xl.save('b.xls')
#Exce表格追加
# from xlutils.copy import copy
# import xlrd
# yuan_file=xlrd.open_workbook('b.xls')
# new_file=copy(yuan_file) #复制文件，并不是直接写入到原文件里
# # 先复制后操作，只有写入功能没有读取功能
# sheet=new_file.get_sheet(0)#获取要操作的标签页，get_sheet（下标位置）
# sheet.write(1,1,1111)
# new_file.save('b.xls')
import time
a=time.time()
print(a)
import time
a=time.localtime()
print(a)
import time
#将结构化时间转换为格式化时间
a=time.strftime('%Y-%m-%d %X',time.localtime())#%X时分秒==%H:%M:%S时分秒
print(a)
#将格式化时间转换为结构化时间
a=time.strptime('2019/09/19 10:05:28','%Y/%m/%d  %X')
print(a)
#2.以结构化时间显示utc时区和本地时区输出是元组类型
a=time.localtime(0)#以结构化时间显示本地时区的时间
print(a)
c=time.gmtime(0)#以结构化时间显示utc时区
print(c)
#3.结构化时间和格式时间相互转换
a=time.strftime('%Y/%m/%d  %X',time.localtime())
#将结构化时间转换为格式化时间输出是字符串类型
print(a)
a=time.strptime('2019/09/18 10:52:16','%Y/%m/%d  %X')
#将格式化时间转换为结构化时间
print(a)
#4.将结构化时间转换为时间戳
# a=(2019,9,18,10,52,16,2,261,-1)
# b=time.mktime(a)
# print(b)
#5.sleep(secs)休眠时间
# from time import  sleep
# start=time.time()#开始时间
# for i in range(3):
#     sleep(3)
#     print(i)
# end=time.time()#结束时间
# print(end-start)#结束时间减去开始时间得到花费时间