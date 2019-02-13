# -*- coding: utf-8 -*-
#第一行是保证文件直接在unix、linux、mac上直接执行；第二行注释表示使用UTF-8编码

'the first string'
#任何文件的第一个字符串，表示模块的文档注释
__author__ = 'zhangxw1986'
#表示作者

#以上就是python模块的标准文件模板；接下来才是真正的文件

#定制类：
#(1)__slots__、__len__()前面也已介绍过：slots限定可添加的属性，__len__()是为了能让class作用于len()函数

#(2)__str__():返回用户看到的字符串；可以让显示对象时 显示更好看的字符串
#(3)__repr__:返回程序开发者看到的字符串，也就是说__repr__是为调试服务的。
class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student Object (name: %s)' % self.name
    __repr__ = __str__

#(4)__iter__()方法：使类可以被用于for...in 循环，类似list或tuple那样，该方法返回一个迭代对象。python程序就会不断调用该对象的__next__()方法，
#拿到下一个循环值，直到遇到StopIteration错误时退出循环。
#(5)__getitem__属性:为了使类能像list那样拿到第n个item
#(6)与之对应的是：__setitem__、__delitem__
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a > 100:
            raise StopIteration
        return self.a
    
    def __getitem__(self,n):
        
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L=[]
            for x in range(stop):
                if x >= start:
                    L.append(x)
                a,b = b,a+b
            return L

#(7)_getattr__()方法：动态返回不存在的属性;只有在class中没有定义该属性时，才会调用__getattr__
#(8)__call__方法：可以直接对实例进行调用,调用__call__时还可以带入参数，对实例进行直接调用就好比对一个函数
#进行调用一样，所以可以把对象看成函数，把函数看成是对象，
#(9)问题：既然对象和函数都一样，该如何区别两者呢?这个问题可转换为我们如何判断一个对象是否可以被调用呢？能被调用
#的对象就是一个Callable对象，比如函数和定义的Tearcher类实例（带有__call__()方法）
class Teacher(object):
    def __init__(self,name):
        self.__name = name
    def __getattr__(self,n):
        if n == 'sex':
            return 'female'
        raise AttributeError('\'Student\' object has no attributes \'%s\' '% n)
    def __call__(self):
        print('Teacher\'s name is : %s' % self.__name)

#使用__getattr__()方法调用rest api：
class Chain(object):
    def __init__(self,path=''):
        self.__path = path
    def __getattr__(self,path):
        return Chain('%s/%s' % (self.__path,path))
    def __str__(self):
        return self.__path
    __repr__ = __str__



if __name__ == '__main__':
    s = Student('zxw')
    print(s)
    for n in Fib():
        print(n)
    f = Fib()
    print(f[1],f[2],f[3],f[4])
    print(f[1:5],f[:10])

    t = Teacher('wang')
    # print(t.sex,t.age)
    t()
    print('Teacher object is callable?',callable(t))
    print('Student object is callable?',callable(s))
    print(Chain().status.url.api)

