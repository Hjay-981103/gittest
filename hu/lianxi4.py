#!/usr/bin/python
#-*-coding:utf-8-*-
import socket
#socket：本机自带的模块  作用：socket：套接字，封装的源端口号
#目的端口号，源IP和目的IP，提供双方的通信的功能
#tcp协议  通信
#服务器端
#创建一个套接字（创建一个有接受能力和发送能力的对象）
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#AF_INET:代表的是IPV4
#SOCK_STREAM  TCP套接字类型
#SOCK_DGRAM  UDP套接字类型
s.bind(('192.168.10.50',84))
#监听，启用服务器以接受连接
s.listen(3)
while True:
    #接受请求
    #第一个值，建立连接的信息
    #第二个值，客户端的ip地址和端口号
    client,addr=s.accept()
    #接收客户端发送的请求最大1024个字节
    recive=client.recv(1024)
    #将接受过来的信息解码打印
    print(recive.decode('utf8'))
    #发送响应
    #输入放松相应
    reponse=input('请响应：')
    #将输入的内容进行发送