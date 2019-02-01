#使用列表list和元组tuple

cls = [ '你好','fadc','是的']


cls.append('123321')
print(cls[-1])
cls.insert(2,'cba')
print(cls)
cls.pop(2)
print(cls)

tp = (1,2,3)
print(len(tp))
tp1 = (1,)
print(type(tp1))