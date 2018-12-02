### Implement a MyQueue class which implements a queue using two stacks.

from utils import Stack

class MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, item):
        self.s1.push(item)

    def dequeue(self):
        if self.s2.top is None:
            while self.s1.top is not None:
                self.s2.push(self.s1.pop())
        return self.s2.pop()

def test():
    q = MyQueue()
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(5)
    print(q.dequeue())
    q.enqueue(4)
    print(q.dequeue())

test()
