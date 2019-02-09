#生成器

g = (x for x in range(1,11))
# print(g)
# for m in g:
#     print(m)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 5
o = odd()
print(next(o))
print(next(o))
print(next(o))


def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n= n + 1
    return 0
f = fib(10)
print(next(f))
print(next(f))
print(next(f))
print(next(f))