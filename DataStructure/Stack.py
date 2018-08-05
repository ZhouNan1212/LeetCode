# -*- coding: utf-8 -*-
class Stack(object):
    # 初始化栈为空列表
    def __init__(self):
        self.items = []

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.items == []

    # 返回栈顶元素
    def peek(self):
        return self.items[len(self.items) - 1]

    # 返回栈的大小
    def size(self):
        return len(self.items)

    # 把新的元素堆进栈里面（程序员喜欢把这个过程叫做压栈，入栈，进栈……）
    def push(self, item):
        self.items.append(item)

    # 把栈顶元素丢出去（程序员喜欢把这个过程叫做出栈……）
    def pop(self):
        return self.items.pop()  # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
