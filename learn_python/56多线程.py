import time,threading

#新线程执行的代码:
def loop():
    print('threading %s is running ...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
    print('balance num is :',balance)

def run_thread(n):
    for i in range(n):
        lock.acquire()
        try:
            change_it(i)
        finally:
            lock.release()

if __name__ == "__main__":
    # print('thread %s is running ...' % threading.current_thread().name)
    # t = threading.Thread(target=loop,name='LoopThread')
    # t.start()
    # t.join()
    # print('threading %s ended.' % threading.current_thread().name)

    run_thread(10)