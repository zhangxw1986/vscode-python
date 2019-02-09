#高阶函数
from functools import reduce
#(一)map函数
def f(x):
    return x * x

r = map(f,[1,2,3,4,5,6,7,8,9,10])
print(list(r))

#(二)reduce函数：1）str转换成int的函数
def fn(x,y):
    return 10*x + y
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

result = reduce(fn,map(char2num,'134578'))
print(result)

#reduce函数：2)str转换成int写成一个函数
def str2int(s):
    def fn1(x,y):
        return 10*x + y
    def char2num1(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(fn1,map(char2num1,s))
str = '12341231'
result1 = str2int(str)
print(result1)

#(三)filter函数：
#筛选出奇数
def isOdd(n):
    return n % 2 == 1
print(list(filter(isOdd,[1,23,4,5,6,7,89,0])))

#筛选：去掉序列中的空字符串
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['A  ','  ','B  B  B','   ',None])))

#筛选：获取素数
def  _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x : x % n >0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n 
        it = filter(_not_divisible(n),it)

for  n  in primes():
    if n < 100:
        # print(n)
        pass
    else:
        break

#(四) sorted函数
print(sorted([2,432,2,53,-1231,32,11]))
print(sorted([2,432,2,53,-1231,32,11],key=abs))
print(sorted(['bob','about','Zoo','Credit']))
print(sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True))