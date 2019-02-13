# -*- coding: utf-8 -*-
#第一行是保证文件直接在unix、linux、mac上直接执行；第二行注释表示使用UTF-8编码

'the first string'
#任何文件的第一个字符串，表示模块的文档注释
__author__ = 'zhangxw1986'
#表示作者

#以上就是python模块的标准文件模板；接下来才是真正的文件

#(1)__slots__:如果我们想要限制实例的属性，就可以在定义class的时候，顶一个一个特殊的变量__slots__，来限制class
#实例能添加的属性

from types import MethodType
class Student(object):
  __slots__ = ('name','score','setAge','setScore','age')
  pass


#(2)使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的。
#(3)如果在子类中也定义__slots__,这样子类允许定义的属性就是自身的slots加上父类的slots
class MidStudent(Student):
  pass

def setAge(self,age):
  self.age = age

#要想所有实例都绑定方法，需给class绑定方法
def setScore(self,score):
  self.score = score


if __name__ == '__main__':
  s = Student()
  s.name = 'zxw'
  print(s.name)
  s.setAge = MethodType(setAge,s)
  s.setAge(5)
  print(s.age)

#给一个实例绑定的方法，对另一个实例不起作用
  # s2 = Student()
  # s2.setAge(26)
  # print(s2.age)

  Student.setScore = setScore
  s3 =  Student()
  s3.setScore(90)
  print(s3.score)

  mid = MidStudent()
  mid.sex = "female"
  print(mid.sex)