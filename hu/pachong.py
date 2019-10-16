#!/usr/bin/python
# -*-coding:utf-8-*-
# import re
# #
# import requests
# a='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1569039724835&di=51937976a8c5d17044a3284021f1721e&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201407%2F24%2F20140724205549_UMiaH.jpeg'
# # #a='https://video.pearvideo.com/mp4/adshort/20190918/cont-1603851-14399999_adpkg-ad_hd.mp4'
# # for i in range(1239527):
# #   a = 'https://www.xbiquge6.com/77_77363/{}.html'.format(i)
# b = requests.get(a)  # 请求网址的
#   #print(b)
# # '''接受响应内容的第一种'''
# #
#   #c=b.text('utf-8') #以文本格式接收
# #print(c)
# # '''接收响应内容的第二种content：以字节的方式接收'''
# # c=b.content.decode('utf-8')
# c=b.content.decode('')
# print(c)
# # #将爬的内容写进文件里
# txt = open(r'E:\PycharmProjects\untitled\223.txt',mode='w',encoding='utf-8')
# d=txt.write(c)
# d=txt.close()
# with open('a.mp4','wb') as f:  #爬取视频资源格式为MP4
#     f.write()
# 过滤
# zifu='4wqw\nQfwq123qfQwqw4'
# guolv=re.compile('q(.*?)q',re.S)
# answer=re.findall(guolv,zifu)
# guolv.findall(zifu)
# answer1=guolv.findall(zifu)
# print(answer1)
# guolv=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br /><br />')
# answer=guolv.findall(c)
# for i in answer:
#      print(i)
#   txt=open(r'E:\PycharmProjects\untitled\223.txt',mode='w',encoding='utf-8')
#   txt.write(c)
# txt.close()
#import json
# import requests
# #loads:反序列化(就是将json格式转换为python的字典格式)
# # a=json.loads('{"result":{"data":12}}')
# # print(a['result']['data'])
# #a='https://map.baidu.com/?qt=subwayscity&t=1569032000551'
# #head={'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
# a='https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2561439800.jpg'
# b=requests.get(a)
# geshi=b.text
# # result=json.loads(geshi)
# i = 0
# while True:
#     try:
#        city=result['subways_city']['cities'][i]['cn_name']
#        i+=1
#        print(city)
#     except:
#       break
# import re
# import json
# import requests
# import os
# a='https://www.zhipin.com/wapi/zpCommon/data/oldindustry.json'
# b=requests.get(a)
# geshi=b.text
# result=json.loads(geshi)
# i = 0
# while True:
#     try:
#        name=result['zpData']['code'][i]['name']
#        i+=1
#        print(name)
#     except:
#       break

# import json
# import requests
# url='https://sou.zhaopin.com/?p=2&jl=765&sf=0&st=0&kw=软件测试工程师kt=3'
# head={'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
# html=requests.get(url,head)
# geshi=html.text
# result=json.loads(geshi)
# with open ('qwe.txt','w',encoding='utf-8') as a:
#     a.write(('斌斌'+'\n')*20)
# with open('qwe.txt','r+',encoding='utf-8') as b:
#
#     for i in range(15,21):
#        b.readlines(i)
#        print(b)
#paramiko 封装了ssh协议，主要用于远程控制
import paramiko
#首先需要一个ssh的客户端用来连接主机
# ssh123=paramiko.SSHClient()
# #将第一次的连接的主机跳过验证，并添加到know_host文件中
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh123.connect(hostname='192.168.2.113',
#                port=22,
#                username='root',
#                password='123456')
# stuin,stuout,stuerr=ssh123.exec_command('ls -al')
# #stuin：指的是你输入的命令,直接有结果的命令
# #stuout：命令运行后的结果
# #stuerr：命令的报错
# aa=stuout.read().decode('utf-8')
# print(aa)
# ssh123.close()
#使用paramiko模块中的sftpclinet组件传输文件
#1.建立一个传输通道，填入IP地址和端口号
import paramiko
transport=paramiko.Transport(('192.168.2.113',22))
#2.连接主机，只需要输入用户名和密码
transport.connect(username='root',password='123456')
#3.创建一个sftp客户端
sftp_client=paramiko.SFTPClient.from_transport(transport)
#4.从linux传文件到Windows
#sftp_client.get('a.txt',r'E:\a.txt')
#5.从windows上传文件到linux
# sftp_client.put(r'E:\a.txt','/root/a.txt')
#6.在linux上创建目录
# sftp_client.mkdir('/root/text')
#7.rename给目录重命名
# sftp_client.rename('text','text1')
#8.remove删除目录
# sftp_client.remove('text1')

