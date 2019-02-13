# -*- coding: utf-8 -*-
#第一行是保证文件直接在unix、linux、mac上直接执行；第二行注释表示使用UTF-8编码

'the first string'
#任何文件的第一个字符串，表示模块的文档注释
__author__ = 'zhangxw1986'
#表示作者

#以上就是python模块的标准文件模板；接下来才是真正的文件

#(1)通过多重继承，一个子类就可以同时获得多个父类的所有的功能。
#(2)MixIn混入类：在设计类的继承关系时，主线通常都是单一继承下来的。如果要混入额外的功能，通过多重继承就可以实现。
#(3)MixIn的目的就是给一个类增加多个功能，这样在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，
#而不是设计多层次的复杂的继承关系。
class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class RunnableMixIn(object):
    def run(self):
        print('running....')

class FlyableMixIn(object):
    def fly(self):
        print('fly....')

class Dog(Mammal,RunnableMixIn):
    pass

class Bat(Mammal,FlyableMixIn):
    pass

class Parrot(Bird,FlyableMixIn):
    pass

class Ostrich(Bird,RunnableMixIn):
    pass


if __name__ == '__main__':
    d = Dog()
    d.run()
    p = Parrot()
    p.fly()