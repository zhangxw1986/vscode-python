# -*- coding: utf-8 -*-
#第一行是保证文件直接在unix、linux、mac上直接执行；第二行注释表示使用UTF-8编码

'32 类和实例'
#任何文件的第一个字符串，表示模块的文档注释
__author__ = 'zhangxw1986'
#表示作者

#以上就是python模块的标准文件模板；接下来才是真正的文件




class Student(object):

    def __init__(self,name,score):
        self.__name =  name
        self.__score = score


    def printScore(self):
        print(self.__name,self.__score)

    def getName(self):
        print(self.__name)
    def getScore(self):
        print(self.__score)
    def setName(self,name):
        self.__name = name
    def setScore(self,score):
        self.__score = score

    def getGrade(self):
        if self.__score >0:
            return 'A'
        else:
            return 'C'

class MidStudent(Student):
    def __init__(self,name,score,age):
        super(MidStudent,self).__init__(name,score)
        self.__age = age
    def getAge(self):
        print(self.__age)
    def setAge(self,age):
        self.__age = age

if __name__ == '__main__':
    bar = Student('carl',93)
    # print(bar.name)
    bar.name = 'jane'
    print(bar.name)
    bar.getName()
    bar.setName('odele')
    bar.getName()
    print(bar._Student__name)