# -*- coding: utf-8 -*-
#第一行是保证文件直接在unix、linux、mac上直接执行；第二行注释表示使用UTF-8编码

'the first string'
#任何文件的第一个字符串，表示模块的文档注释
__author__ = 'zhangxw1986'
#表示作者

#以上就是python模块的标准文件模板；接下来才是真正的文件


#(1)异常处理机制：当某些代码可能存在问题时,可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳到
#   错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此执行完毕。
#(2)如果没有错误发生，except语句块不会执行，但是finally如果有，则一定会被执行。
#(3)错误可能有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理。可以由多个except语句块来捕获不同类型的错误。
#(4)python的错误实际上也是class，所有的错误类型都继承自BaseException,所以在使用except时需要注意的是，它不但捕获该类型的
#错误，还把其子类也“一网打尽”。


# try:
#     print('try...')
#     a =  input('input number or string:')
#     r = 10 / int(a)
#     print(r)
# except ValueError as e:
#     print('ValueError:',e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:',e)
# finally:
#     print('finally...')
# print('END')


#(5)不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。这样一来,就大大减少了写try...except...finally的麻烦。
def foo(s):
    return 10 / int(s)
def bars(s):
    return foo(s)*2
def main():
    try:
        bars('0')
    except Exception as e:
        print('Error:',e)
    finally:
        print('finally...')

# def foo1(s):
#     n = int(s)
#     if n == 0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n

# def bar1():
#     try:
#         foo1('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise
#     finally:
#         print('finally...')
    
if __name__ == '__main__':
    main()
    # bar1()


