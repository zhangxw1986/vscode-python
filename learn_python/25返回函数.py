#返回函数

def lazy_sum(*args):
    b = 0
    def sum():
        ax = 0
        for n in args:
            ax = ax + n 
        return ax
    return sum

f = lazy_sum(1,3,5,7,9)
print(f)
print(f())

#引入闭包概念：内部函数引用了外部函数的参数和局部变量，当返回函数时，相关参数和变量都保存在返回的函数中，这种称为"闭包"。
f1 = lazy_sum(1)
print(f1())

#闭包导致的问题：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
#如果确实有这样的需求，解决方法是再创建一个函数，用该函数的参数绑定循环变量当前的值
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()
print(f1(),f2(),f3())

#解决方法：
def count1():

    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f4,f5,f6 = count1()
print(f4(),f5(),f6())