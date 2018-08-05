# -*- coding: utf-8 -*-
class Queue(object):  # 无限长队列，这里可以设置队列长度
    # 初始化队列为空列表
    def __init__(self):
        self.items = []

    # 判断队列是否为空，返回布尔值
    def is_empty(self):
        return self.items == []

    # 返回队列的大小
    def size(self):
        return len(self.items)

    # 返回队首的元素
    def queue_first(self):
        return self.items[0]

    # 返回队尾的元素
    def queue_last(self):
        return self.items[len(self.items) - 1]

    # 将一个元素插入队列
    def enqueue(self, element):
        return self.items.append(element)

    # 队首元素出队列
    def dequeue(self):
        first = self.items[0]
        del self.items[0]
        return first


if __name__ == "__main__":
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)

    s.dequeue()





