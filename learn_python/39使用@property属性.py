# -*- coding: utf-8 -*-
#第一行是保证文件直接在unix、linux、mac上直接执行；第二行注释表示使用UTF-8编码

'the first string'
#任何文件的第一个字符串，表示模块的文档注释
__author__ = 'zhangxw1986'
#表示作者

#以上就是python模块的标准文件模板；接下来才是真正的文件

#(1)@property属性：为了避免显示使用setter和getter方法，而让读写变量像属性一样直接使用，可以使用@property
#例如 s.getScore()或s.setScore(score)使用起来比较麻烦，不如直接使用属性那样方便

#(2)@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，减少程序的bug
class Student(object):
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an interger!')
        if value < 0 or value >100:
            raise ValueError('score must between 0 and 100 !')
        self.__score = value
    

if __name__ == '__main__':
    s = Student()
    s.score =99
    print(s.score)