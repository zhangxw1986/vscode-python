from enum import Enum

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dev'))

print(dir(Month))
# print(Month.__mumbers__)
# -*- coding: utf-8 -*-
#第一行是保证文件直接在unix、linux、mac上直接执行；第二行注释表示使用UTF-8编码

'the first string'
#任何文件的第一个字符串，表示模块的文档注释
__author__ = 'zhangxw1986'
#表示作者

#以上就是python模块的标准文件模板；接下来才是真正的文件

#******Enum:可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较
#(1)python定义enum常量最好的办法是：定义一个class类型，然后每个常量都是class的一个唯一实例
#(2)python提供了Enum类来实现这个功能：
#(3)value属性是自动赋值给成员的int常量，默认从1开始
from enum import Enum
Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

print(Month.__members__)
print(dir(Month))
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)
    
#(4)如果需要精确的控制枚举类型，可以从Enum派生出自定义类：即可用成员名称引用枚举常量，也可以根据value的值获得枚举常量
#(5)@unique帮我们检查是否有重复的值
from enum import Enum,unique
@unique
class Weekend(Enum):
    SUN,MON,TUE,WED,THU,FRI,SAT = 0,1,2,3,4,5,6



if __name__ == '__main__':
    print(Weekend.SUN)
    print(Weekend['SUN'])
    print(Weekend.SUN.value)
    print(Weekend(0),Weekend(1))
