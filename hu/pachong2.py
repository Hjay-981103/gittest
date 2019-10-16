#!/usr/bin/python
#-*-coding:utf-8-*-
#面向对象
# import requests
# import re


# class Douban(object):
#     def qing_qiu(self, page):
#         url = f'https://movie.douban.com/top250?start={page}&filter='
#         head = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
#         }
#         # 发送请求，并将结果赋值给res
#         res = requests.get(url=url, headers=head)
#         # 读取结果
#         h = res.content.decode('utf-8')
#         return h
#
#     def guo_lv(self, html):
#         patt = re.compile(r'<span class="title">(.*?)</span>', re.S)
#         items = patt.findall(html)
#
#         for i in items:
#             if '&nbsp' in i:
#                 items.remove(i)
#         return items
#
#     def save(self, shuju):
#         with open('a.txt', 'a', encoding='utf-8') as f:
#             for i in shuju:
#                 f.write(i + '\n')
#
#
# dd = Douban()
# for i in range(25, 100, 25):
#     hh = dd.qing_qiu(i)
#     shuju = dd.guo_lv(hh)
#     dd.save(shuju)
#面向过程
# import requests
# import re
# url='https://movie.douban.com/top250?start=25&filter='
# head={'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
# res=requests.get(url=url,headers=head)
# h=res.content.decode('utf-8')
# patt=re.compile(r'<span class="title">(.*?)</span>',re.S)
# items=patt.findall()
    


#
# import xlrd
# f=xlrd.open_workbook('a.xls')
# sheet=f.sheets()[0]
# new_f=copy(f)
# sheet1=new_f.get_sheet(0)
# if sheet.nrows==0:
#     sheet.nrows(0,0,'内容')
# else:
#     sheet1.write(sheet.nrows,0,'内容')
# new_f.save('a.xls')
# import requests
# import re
# import json
# class Xiaoshuo(object):
#      def qing_qiu(self):
#         a='http://top.hengyan.com/'
#         b= {
#             'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
#         }
#         c=requests.get(url=a,headers=b)
#         h=c.res.contest.get('utf-8')
#         return h
#      def guo_lv(self,html):
#          d=re.compile(r'<li><a href="">(.*?)</a></li>',re.S)
#          items=d.findall(html)
#          for i in items:
#              if "/xiazai/" in i:
#                 items.remove=(i)
#                 return items
#
#      def save(self, shuju):
#         with open('b.txt', 'a', encoding='utf-8') as f:
#             for i in shuju:
#                 f.write(i + '\n')
# dd = Xiaoshuo()
# for i in (34,61,1):
#    hh = dd.qing_qiu(i)
#    shuju = dd.guo_lv(hh)
#    dd.save(shuju)
# d=[]
# import xlwt
# import xlrd
# with open('qwe.txt','w',encoding='utf-8') as a:
#     a.write((' a,b,c,d'+'\n' )*10)
# with open('qwe.txt','r', encoding='utf-8') as a:
#     xl= xlwt.Workbook (encoding= 'utf-8' )
#     b=xl.add_sheet('123')
#     for i ,s in enumerate (a. readlines() ):
#         s=s. split(',')
#         for j,m in enumerate(s) :
#             b. write(i,j,m)
#     xl. save('b.xls' )
# with open('qwe.txt','w', encoding=' utf-8') as a:
#     rd= xlrd. open_workbook('b.xls' )
#     aa= rd.sheet_by_name('123' )
#     hangshu=aa.nrows
#     for i in range (1, hangshu) :
#        rd=','.join(aa.row_values(i))
#        a.write(rd)
# def jiujiu():
#     for i in range(10):
#         for j in range(1,i+1):
#             print('{}*{}={}'.format(j,i,i*j),end=' ')
#         print()
# if __name__=='__main__':
#  jiujiu()






