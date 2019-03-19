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

# def quadratic(a=2,b=4,c=2):
#     if not(a+b+c,isinstance(int,float)):
#         raise TypeError("数据类型不对")
#     d=b**2-4*a*c
#     if d==0:
#         return '%.2f' % ((-b+math.sqrt(d))/(2*a))
#     elif d>0:
#         return '%.2f,%.2f' % ((-b+math.sqrt(d))/(2*a),(-b-math.sqrt(d))/(2*a))
#     else:
#         return ''

# print('quadratic(2, 4, 1) =', quadratic(2, 4, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
# print('quadratic(1, 2, 1) =', quadratic(1, 2, 1))
# print('quadratic(1, 3, 1) =', quadratic(1, 3, 1))
# print('quadratic() =', quadratic())

# # 当不按顺序提供部分默认参数时，需要把参数名写上
# # 定义默认参数要牢记一点：默认参数必须指向不变对象！
# print('quadratic(a=2,c=1) =', quadratic(2,c=1))

# def add_end(L=[]):
#     L.append('end')
#     return L
# print(add_end([1]))
# print(add_end([1]))
# print(add_end())
# print(add_end())


# #可变参数 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# print(calc(1,2,3,4))
# #*nums表示把nums这个list的所有元素作为可变参数传进去。
# t=(1,2,3)
# print(calc(*t))

# #关键字参数 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
# #**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)

# extra={'city': 'Beijing', 'job': 'Engineer'}
# print(person('Jack', 24, **extra))
# print(person('Jack', 24, **{'city': 'Beijing', 'job': 'Engineer'}))
# print(person('Jack', 24, city="Beijing",job="Engineer"))

# #命名关键字参数 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# #函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*
# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)
# b=(1,2)
# person("a",12,*b,city="beijing",job="123")

# def product(*t):
#     if len(t)<=0:
#         raise TypeError("没参数")
#     sum=1
#     for x in t:
#         sum=sum*x
#     return sum

# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')

# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# *args 是可变参数 接收的是一个tuple元祖
# **kw 关键字参数 接受的是一个dict(java的map)


# # 递归函数
# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)

# print(fact(10))

# L=[]
# n=99
# while n>0:
#     L.append(n)
#     n=n-2
# print(L)



# # 切片 slice
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# #从0开始取2个
# print(L[0:2]) 
# print(L[-1:])
# #从0 开始取4个 每2个取一个
# print(L[0:4:2])


# D={'Michael': 95, 'Bob': 75, 'Tracy': 85}
# # print(D.keys())
# for d in D:
#     print(d)
# #默认情况下Dict迭代的是 key 可以通过 keys() values() items()来分别迭代key value 每个元素

def findMinAndMax(L):
    # print(len(L))
    if(len(L))<=0:
        return None,None
    a=L[0]
    b=L[0]
    for l in L:
        if(l>a):
            a=l
        elif(l<b):
            b=l
    return b,a


if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功5!')
