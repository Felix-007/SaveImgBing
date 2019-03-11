# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# print("hello", "world!")
# print(2**10)
# name=input("input you name:")
# print("hello",name)
# print("1024*768=",1024*768)

# a=input("input value a=")

# a=1.2e-1;
# if a>0:
#     print(a)
# else:
#     print(-a)

# print('\\\/\\')
# print(r'\\\/'+"\\")

# print(r'''dear
# god
# forgive
# me./n
# ''')

# age=int(input("input you age:"))
# if age>=18:
#     print('成年');
# else:
#     print("未成年");

# a = 'ABC'
# b = a
# a = 'XYZ'
# print(b)

# print(10/3)
# print(9/3)
# #地板除
# print(10//3)

# print("n =" ,123)
# print(r"f = 456.789")
# print("s1","=","Hello,","world")
# print("s2","=",r"Hello, \'Adam\''")
# print("s3 = ",r"r'''Hello,")
# print("Lisa!'''")

# print(ord('1'))
# print(chr(25105))
# print(chr(29233))    
# print(chr(20320)) 

# print('A'.encode('ascii'))
# print('中文'.encode('utf-8'))

# print("hi ,%s , %s,you are a big cat." % ('jack','ss'))

# print('%03d-%03d' % (33.31, 1))
# print('%2.3f' % 123.1415926)

# print("growth rate : %d %%" % 7 )

# print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

# s1=72
# s2=85
# r=85-72
# print('小米成绩提升了:%.1f%%' % r)

# classmate=["A","B","C"]
# print(classmate)
# print(len(classmate))

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(L[0][1])
# print(L[1][1])
# print(L[2][2])

# age = 20
# if age >= 6:
#     print('teenager')
# elif age >= 18:
#     print('adult')
# else:
#     print('kid')

# if 0:
#     print(11)
# else:
#     print(22)

# print("欢迎使用BMI计算器")
# height =float(input("输入你的身高(m):"))
# weight =float(input("输入你的体重(kg):"))
# bmi=weight/(height**2)
# if bmi<=18.5:
#     print("过轻")
# elif bmi<=25:
#     print("正常")
# elif bmi<=28:
#     print("过重")
# elif bmi<32:
#     print("肥胖")
# elif bmi>=32:
#     print("严重肥胖")

# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)

L = ['Bart', 'Lisa', 'Adam']
# for l in L:
#     print("Hello, %s%s" % (l,'!'))

# i=len(L)-1;
# while i>=0:   
#     print("hello,",L[i],"!")
#     i=i-1

# y=0
# while y<len(L):
#     print("hello,",L[y],"!")
#     y=y+1

# n=0
# while n<=100:    
#     print(n)
#     n=n+1
#     if(n>10):
#         break
# print("end")


n=0
# while n<=10:
#     n=n+1
#     if(n%2==0):
#         continue
#     print(n)

#dict=在别的语言中就是map
# d={'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print('Bob' in d)

# help(abs)
# print(max('d1','dc','dc'))
# print(max('2','3','-1'))

# print(bool('a'))

# print(hex(255))
# print(hex(1000))

# def myabs(x):    
#     if(x>=0):
#         return x
#     else:
#         return -x
# print(myabs(0))
# print(myabs(1))
# print(myabs(-99))

# def nop():
#     pass
# print(1)

# print(myabs(1))

# print(not isinstance(1.2,(int,float)))

# def myabs_pro(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError("非法参数")
#     if(x>=0):
#         return x
#     else:
#         return -x
# print(myabs_pro(1.1))

import math
# def move(x,y,step,angle=0):
#     nx=x+step*math.cos(angle)
#     ny=y-step*math.sin(angle)
#     return nx,ny
# print(move(0,0,1,60))

# # # 定义函数时，需要确定函数名和参数个数；

# # # 如果有必要，可以先对参数的数据类型做检查；

# # # 函数体内部可以用return随时返回函数结果；

# # # 函数执行完毕也没有return语句时，自动return None。

# # # 函数可以同时返回多个值，但其实就是一个tuple。

# def quadratic(a,b,c):
#     if not(a+b+c,isinstance(int,float)):
#         raise TypeError("数据类型不对")
#     d=b**2-4*a*c
#     if d==0:
#         return (-b+math.sqrt(b))/(2*a)
#     elif d>0:
#         return
