#!/usr/bin/python
#-*-coding:utf-8-*-
# class Yuangong:         #继承
#     def hanshu(self):
#         print('鄙视')
#     def hanshu1(self):
#         print('凸(￣ヘ￣凸＃)')
# class Student:
#     def __init__(self):
#         self.name='空的'
#     def hanshu(self):
#         print(120)
#     def hanshu1(self):
#         print(110)
# class Kdstudent(Yuangong,Student):
#     pass
# laowang=Kdstudent()
# laowang.hanshu()
# laowang.hanshu1()
#   多态
# class Animal:
#     def talk(self):
#         pass
# class People(Animal):
#     def talk(self):
#         print('你好(*´▽｀)ノノ')
# class Pig(Animal):
#     def talk(self):
#         print('^(*￣(oo)￣)^')
# class Cat(Animal):
#     def talk(self):
#         print('o( =•ω•= )m')
# People().talk()
# Cat().talk()
#   函数重写
# class Student:
#     def hanshu(self):
#         print('(*´▽｀)ノノ')
# class Kdstudent(Student):
#     def hanshu(self):
#         print('凸(￣~￣)凸')
# laowang=Kdstudent()
# laowang.hanshu()
#  家具实例
# class Home:
#     def __init__(self,newarea):
#         self.area= newarea
#         self.containsItems=[]
#     def __str__(self):
#         msg='家当前可用面积为：'+str(self.area)+'平方米'
#         msg+='\n家里目前的家具有：'
#         if len(self.containsItems)>0:
#             for i in self.containsItems:
#                 msg+=i.style+','
#             msg=msg.strip(',')
#         else:
#             msg='当前没有家具'
#         return msg
#     def additems(self,item):
#         if self.area>item.area:
#             self.containsItems.append(item)
#             self.area-=item.area
# class Bed:
#     def __init__(self,newstyle,newarea):
#         self.style=newstyle
#         self.area=newarea
#     def __str__(self):
#         msg='床的面积为：'+str(self.area)+'平方米'
#         msg+='\n床的型号为：'+self.style
#         return msg
# class Desk:
#     def __init__(self,newstyle,newarea):
#         self.style=newstyle
#         self.area=newarea
#     def __str__(self):
#         msg='书桌的面积为：'+str(self.area)+'平方米'
#         msg+='\n书桌的型号为：'+self.style
#         return msg
# home=Home(200)
# print(home)
# bed=Bed('席梦思',4)
# print(bed)
# home.additems(bed)
# print(home)
# desk=Desk('杂牌书桌','1')
# print(desk)