import pickle

#(1)序列化概念:讲变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，其他语言中也被称为serialization，marshalling，
#flattening等等，序列化之后，就可以把序列化后的内容写到磁盘里，或者通过网络传输到别的机器上。
#(2)反序列化：把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
#(3)python提供了pickle模块提供序列化能力。
#(4)pickle作用：由于pickle只是在python上的功能，在其他语言不通用，因此pickle只能保存一些不重要的数据，即使不能成功反序列化也没关系。
d = dict(name='bob',age=20,score=88)
print(pickle.dumps(d))

with open('hello.txt','wb') as f:
    pickle.dump(d,f)

with open('hello.txt','rb') as f:
    d1 = pickle.load(f)

print(d1)

#(5)如果想在不同语言间传递对象，就必须把对象序列化成标准格式，比如XML，JSON。JSON更好：兼容性强，可在web页面直接读取，更快。
#(6)JSON:序列化方法是dumps、dump，是将python的dict对象转换为JSON字符串

import json

d2 = dict(name='bob',age=20,score=88)
print(json.dumps(d))



#(7)JSON反序列化为python对象：用loads()或对应的load()方法。前者是将JSON字符串反序列化，后者是从file-like object读取字符串并反序列化

#(8)那class对象如何转换成JSON字符串？通过对象的__dict__定制变量
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

stu = Student('zxw',32)
print(stu.__dict__)