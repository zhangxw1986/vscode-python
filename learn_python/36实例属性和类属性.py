#!/usr/bin/env python3           
# -*- coding: utf-8 -*-
#第一行是保证文件直接在unix、linux、mac上直接执行；第二行注释表示使用UTF-8编码

'the first string'
#任何文件的第一个字符串，表示模块的文档注释
__author__ = 'zhangxw1986'
#表示作者

#以上就是python模块的标准文件模板；接下来才是真正的文件


#编写程序的时候不要把实例属性和类属性使用相同名字，因为相同名称的实例属性会屏蔽掉类属性
class Student(object):
  name = 'Student'








if __name__ == '__main__':
    s = Student()
    print(s.name)
    s.name = 'bob'
    print(s.name)
    print(Student.name)
    del s.name
    print(s.name)
