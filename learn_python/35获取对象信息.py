         
# -*- coding: utf-8 -*-
#第一行是保证文件直接在unix、linux、mac上直接执行；第二行注释表示使用UTF-8编码

# '32 类和实例'
#任何文件的第一个字符串，表示模块的文档注释
__author__ = 'zhangxw1986'
#表示作者

#以上就是python模块的标准文件模板；接下来才是真正的文件


#(1)判断基本类型、函数、对象都可以使用type
def test():
    print('test function')

class A(object):
    def __init__(self,name):
        self.__name = name
    def getA(self):
        print(self.__name)

class B(A):
    pass

a = A('zxw')    
b = B('zwy')

print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
print(type(test))
print(type(abs))
print(type(a))

#(2)type返回的是class类型，如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
print(type(123) == type(345))
#(3)如果要判断函数是否相等，就需要引入types模块
import types
print(type(test) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType) 
print(type(lambda x:x ) == types.LambdaType)

#(4)使用isinstance：对于class的继承关系来说，使用type()很不方便，我们要判断class的类型，可以使用isinstance
print(isinstance(a,object))
print(isinstance(a,A))
print(isinstance(a,B))
print(isinstance(b,A))
print(isinstance(b,B))
print(isinstance('a',str))
print(isinstance(133,int))

#(5)使用dir()函数：如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print(dir(a))
print(len('abc'))
print('abc'.__len__())

#(6)通过配合使用getattr()、setattr()、hasattr()可以直接操纵一个对象的状态：
print(hasattr(a,'name'))

if __name__ == '__main__':
    # print(type(123))
    # print(type('str'))
    # print(type(None))
    # print(type(abs))
    # print(type(test))
    pass
