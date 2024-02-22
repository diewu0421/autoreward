import threading
import time

mutex_printer = threading.Lock()  # 打印机锁
mutex_scanner = threading.Lock()  # 扫描仪锁


class MyThread1(threading.Thread):

    def run(self):
        mutex_printer.acquire()     # 获取打印机锁
        print('线程1已经获得打印机的使用权')
        time.sleep(1)		# 延时操作是为了保证线程2能够在线程1获得扫描仪锁之前获得扫描仪锁，这样就一定会发生死锁

        mutex_scanner.acquire()     # 再获取扫描仪锁
        print('线程1已经获得扫描仪的使用权')

        mutex_scanner.release()     # 释放扫描仪锁(按获取锁的相反顺序释放锁)
        mutex_printer.release()     # 释放打印机锁(按获取锁的相反顺序释放锁)


class MyThread2(threading.Thread):

    def run(self):
        mutex_scanner.acquire()     # 先获取扫描仪锁
        print('线程2已经获得扫描仪的使用权')
        time.sleep(1)

        mutex_printer.acquire()     # 再获取打印机锁
        print('线程2已经获得打印机的使用权')

        mutex_printer.release()     # 释放打印机锁(按获取锁的相反顺序释放锁)
        mutex_scanner.release()     # 释放扫描仪锁(按获取锁的相反顺序释放锁)



def func1():
    yield 1
    yield from fun2()
    yield 2


def fun2():
    time.sleep(1)

    for i in range(0, 1000):
        yield i
        time.sleep(0.1)

if __name__ == '__main__':
    # t1 = MyThread1()
    # t2 = MyThread2()
    # t1.start()
    # t2.start()

    for i in func1():
        print("i = ", i)
