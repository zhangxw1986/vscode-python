#可变对象，不可变对象：数字、字符串、元组都是不可变对象；list、字典是可变对象
a = 5
b = a
a = a + 2
print(b)


#从动态类型来看参数传递：如果传递的是不可变对象，那么实参改变不会影响外部的不可变对象
def f(x):
    x = 100
    print(x)

f(a)
print(a)

#从动态类型来看参数传递：如果传递的是可变对象引用，那么实参改变可能会影响外部的原对象
def f(x):
    x[0] = 100
    print(x)

l = [1,2,3]
f(l)
print(l)
