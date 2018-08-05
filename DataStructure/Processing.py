# -*- coding: utf-8 -*-
import multiprocessing
import time


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


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=worker_1, args=(2,))
    p2 = multiprocessing.Process(target=worker_2, args=(3,))
    p3 = multiprocessing.Process(target=worker_3, args=(4,))

    p1.start()
    p2.start()
    p3.start()

    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id:" + str(p.pid))
    print("END!!!!!!!!!!!!!!!!!")


    p = ClockProcess(3)
    p.daemon = True  # 子进程设置了daemon属性，主进程结束，它们就随着结束了。
    p.start()
    p.join()

    print("end!")


