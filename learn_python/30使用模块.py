#!/usr/bin/env python3           
# -*- coding: utf-8 -*-
#第一行是保证文件直接在unix、linux、mac上直接执行；第二行注释表示使用UTF-8编码

'the first string'
#任何文件的第一个字符串，表示模块的文档注释
__author__ = 'zhangxw1986'
#表示作者

#以上就是python模块的标准文件模板；接下来才是真正的文件

import sys
#sys模块的argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个元素总是文件的名称
print(sys.argv)

def test():
    args = sys.argv
    print('doing test function')
    if len(args) == 1:
        print('hello! no args!')
    elif len(args) == 2:
        print('hello! one args:',args[1])
    else:
        print('hello! more than one args!')
    return 

#=============关于作用域=================
#1、正常的函数和变量是公开的public
#2、类似于__xxx__的变量是特殊变量，可以被直接引用，但是有特殊用途，比如__author__、__name__、__doc__等
#3、类似_xxx或__xxx这样的函数或变量是私有的private，不应该直接被引用。内部逻辑用的函数或变量用private变量表示。
#外部不需要引用的变量全部用private变量表示，只有外部需要引用的变量采用public

#命令行运行模块文件时，解释器把特殊变量__name__置为__main__,而如果在其他模块导入该模块时，if判断将失败
#这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是测试
