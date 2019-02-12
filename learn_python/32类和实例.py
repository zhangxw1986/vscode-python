# -*- coding: utf-8 -*-
#第一行是保证文件直接在unix、linux、mac上直接执行；第二行注释表示使用UTF-8编码

'32 类和实例'
#任何文件的第一个字符串，表示模块的文档注释
__author__ = 'zhangxw1986'
#表示作者

#以上就是python模块的标准文件模板；接下来才是真正的文件


#类定义语法如下： 关键字class；后面跟类的名字，一般首字母大写；紧接着是(object),表示该类是从哪个类继承下来的；
#如果没有合适的继承类，就使用object类，这是所有类都会继承的类

class Student(object):
#定义构造函数__init__
#注意__init__方法的第一个参数永远是self，表示创建的实例本身，因此在__init__方法内部，就可以把各种属性绑定
#到self，因为self就指向创建的实例本身。
#有了__init__方法，在创建实例的时候就不能传入空的参数了，必须传入与__init__方法匹配的参数。
    def __init__(self,name,score):
        self.name =  name
        self.score = score

#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，
# 不用传递该参数。除此之外，没有区别
    def printScore(self):
        print(self.name,self.score)

    def getGrade(self):
        if self.score >0:
            return 'A'
        else:
            return 'C'

class MidStudent(Student):
    def __init__(self,name,score,age):
        super(MidStudent,self).__init__(name,score)
        self.age = age

if __name__ == '__main__':
    bar = Student('bb',99)
    bar.size = "D"
    print(bar)
    print(Student)
    bar.printScore()
    print(bar.getGrade())

    mid = MidStudent('carl',98,10)
    print(mid.printScore())