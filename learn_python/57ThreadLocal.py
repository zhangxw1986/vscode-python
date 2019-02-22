import threading

#(1)全局ThreadLocal对象:多线程环境下，每个线程都有自己的局部变量而互不影响。ThreadLocal对象就是一个全局dict，每个thread都可以对他读写，但互不影响。
#(2)ThreadLocal最常用的场景：为每个线程绑定一个数据库连接，HTTP请求，用户身份认证等等，这样一个线程所有调用到的处理函数
#都可以非常方便的访问这些资源
#(3)join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步.

local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello,%s (in %s)' % (std,threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

if __name__ == "__main__":
    t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
    t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
