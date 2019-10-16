#!/usr/bin/python
#-*-coding:utf-8-*-
#客户端
#客户端不需要绑定ip和监听
import socket
while True:
    #创建一格套件
    sock=socket.socket()
    #客户端虽然不需要绑定ip，但是连接服务器
    sock.connect(('192.168.10.50',84))
    #发送请求
    #输入请求的内容
    message=input('请输入你的内容：')
    #发送请求的内容给服务器
    sock.send(message.encode('utf8'))
    #接收服务器的响应
    revice=sock.recv(1024)
    print(revice.decode('utf8'))
    #断开连接
    # sock.close()
