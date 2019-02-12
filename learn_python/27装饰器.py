import functools
#装饰器

#无参的装饰器
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' %func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2019-2-9')

print(now())

#有参的装饰器
def log1(text):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log1('hahahh')
def now1():
    print('2020-2-10')
print(now1())
print(now1.__name__)


