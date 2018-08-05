# -*- coding: utf-8 -*-
import multiprocessing
from multiprocessing import Pool
import time
import os
import random


def worker(interval):
    n = 5
    while n > 0:
        print("The time is {0}".format(time.ctime()))
        time.sleep(interval)
        n -= 1


def worker_1(interval):
    print("worker_1")
    time.sleep(interval)
    print("end worker_1")


def worker_2(interval):
    print("worker_2")
    time.sleep(interval)
    print("end worker_2")


def worker_3(interval):
    print("worker_3")
    time.sleep(interval)
    print("end worker_3")


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


# 将进程定义为类, 进程p调用start()时，自动调用run()
class ClockProcess(multiprocessing.Process):

    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        n = 5
        while n > 0:
            print("the time is {0}".format(time.ctime()))
            time.sleep(self.interval)
            n -= 1


class PrintProcess(multiprocessing.Process):

    def __init__(self, num):
        multiprocessing.Process.__init__(self)
        self.num = num

        print("The number of CPU is:" + str(multiprocessing.cpu_count()))
        for p in multiprocessing.active_children():
            print("child   p.name:" + p.name + "\tp.id:" + str(p.pid))
        print("END!!!!!!!!!!!!!!!!!")

    def run(self):
        print(self.num)


if __name__ == "__main__":
    # p1 = multiprocessing.Process(target=worker_1, args=(2,))
    # p2 = multiprocessing.Process(target=worker_2, args=(3,))
    # p3 = multiprocessing.Process(target=worker_3, args=(4,))
    #
    # p1.start()
    # p2.start()
    # p3.start()
    #
    # print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    # for p in multiprocessing.active_children():
    #     print("child   p.name:" + p.name + "\tp.id:" + str(p.pid))
    # print "END!!!!!!!!!!!!!!!!!"

    # print('Process (%s) start...' % os.getpid())
    # # Only works on Unix/Linux/Mac:
    # """
    # 普通的函数调用，调用一次，返回一次，但是 fork() 调用一次，返回两次，
    # 因为操作系统自动把当前进程（父进程）复制了一份（子进程），然后，分别在父进程和子进程内返回。
    # 子进程永远返回 0，而父进程返回子进程的 ID。
    # """
    pid = os.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

    print('Parent process %s.' % os.getpid())
    """
    创建子进程时，只需要传入一个执行函数和函数的参数（target 指定了进程要执行的函数，args 指定了参数）。
    创建好进程 Process 的实例后，使用 start() 方法启动。join() 方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    """
    # p = multiprocessing.Process(target=run_proc, args=('test',))
    # print('Child process will start.')
    # p.start()
    # p.join()
    # print('Child process end.')



