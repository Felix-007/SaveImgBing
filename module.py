# !/usr/bin/env python3
# -*- coding: utf-8 -*-

#模块学习
'a test module'

__author__='Felix'

import sys
import math

# def test():
#     args=sys.argv
#     if len(args)==1:
#         print('Hello, world!')
#     elif len(args)==2:
#         print('Hello, %s!' % args[1])
#     else:
#         print('Too many arguments!')

# if __name__=='__main__':
#     test()

# # 类似__xxx__这样的变量是特殊变量，可以被直接引用，
# # 但是有特殊用途，比如上面的__author__，__name__就是特殊变量，
# # hello模块定义的文档注释也可以用特殊变量__doc__

# # 类似_xxx和__xxx这样的函数或变量就是非公开的（private），
# # 不应该被直接引用，比如_abc，__abc等；

# print(sys.path)


# class Strudent(object):
#     def __init__(self,name,score,age):
#         self.name=name
#         self.score=score
#         self.__age=age
#     def print_socre(self):
#         print('%s:%s' % (self.name,self.score))

#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'
#     def get_age(self):
#         return self.__age
#     def set_age(self,age):
#         self.__age=age 

# bart=Strudent('bart',59,12)

# bart.print_socre()

# # class后面接大写的类名  括号里面是继承的类
# # 注意：特殊方法“__init__”前后分别有两个下划线！！ self必须第一个 调用不用传入
# sam=Strudent('sam',89,12)
# sam.name='sam1'
# print(sam.name)

# lisa = Strudent('Lisa', 99,13)
# bart = Strudent('Bart', 59,23)
# print(lisa.name, lisa.get_grade())
# print(bart.name, bart.get_grade())

# print(lisa.get_age())
# print(lisa.set_age(33))
# print(lisa.get_age())

#比如_name，这样的实例变量外部是可以访问的，
# 但是，按照约定俗成的规定，当你看到这样的变量时
# “虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

# __可以通过_Student__name 来访问
# print(bart.__age)
# print(bart._Strudent__age)

# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender
#     def get_gender(self):
#         return self.__gender
#     def set_gender(self,gender):
#         self.__gender=gender


# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')


#类的集成和多态
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('dog is Running')
class Cat(Animal):
    def run(self):
        print('cat is Running')

dog=Dog()
dog.run()
cat=Cat()
cat.run()

print(isinstance(dog,Animal))

# 静态语言 vs 动态语言
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，
# 否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。
# 我们只需要保证传入的对象有一个run()方法就可以了
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的

isinstance([1, 2, 3], (list, tuple))
#可同时判断多个类型
#优先使用isinstance()判断类型

#获取一个对象的所有属性和方法  使用dir函数
print(dir(dog))

#就像JAVA里面的getset方法
# getattr()、setattr()以及hasattr()(有属性'xxx'吗)，
# 我们可以直接操作一个对象的状态
print(hasattr(dog,'run'))

