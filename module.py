# !/usr/bin/env python3
# -*- coding: utf-8 -*-

#模块学习
'a test module'

__author__='Felix'

import sys

def test():
    args=sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

# 类似__xxx__这样的变量是特殊变量，可以被直接引用，
# 但是有特殊用途，比如上面的__author__，__name__就是特殊变量，
# hello模块定义的文档注释也可以用特殊变量__doc__

# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），
# 不应该被直接引用，比如_abc，__abc等；
