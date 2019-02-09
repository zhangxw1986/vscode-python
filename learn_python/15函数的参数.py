#函数的参数：位置参数、默认参数、可变参数、关键字参数

#1、位置参数
def power(x):
    return x * x
print(power(10))

def power1(x,n):
    result = 1
    while n >0:
        result *= x
        n = n -1
    return result
print(power1(5,3))

#2、默认参数
def power2(x,n=2):
    result = 1
    while n > 0:
        result *= x
        n = n - 1
    return result
print(power2(5))

#3、可变参数
def calc(*numbers):
    sum = 0
    for  n in numbers:
        sum += n*n
    return sum
# print(calc(1,2,3,4,5,6,7,8,9,10))
num = (1,2,3,4,5,6,7,8,9,10)
print(calc(*num))

#4、关键字参数
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
    return 
print(person('bob',24))
print(person('bob',24,city='beijing'))
print(person('bob',24,city='beijing',gender='M'))
extra = {'city':'changchun','gender':'F'}
print(person('jane',21,**extra))
    
#5、命名关键字参数
def person1(name,age,*,city,gender):
    print('name:',name,'age:',age,'city:',city,'gender:',gender)
    return
print(person1('chr',24,city='nanjing',gender='M'))
# print(person1('chr',24,last_city='nanjing',gender='M'))

#6、参数组合
#函数的参数可以组合使用，组合的顺序是：位置参数、默认参数、可变参数、命名关键字参数、关键字参数