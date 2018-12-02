### How would you design a stack which, in addition to push and pop,
### also has a function min which returns the minimum element? Push,
### pop and min should all operate in O(1) time.

from utils import Stack

class NodeWithMin:
    def __init__(self, d):
        self.val = d
        self.nxt = None
        self.min_val = d

class StackWithMin:
    def __init__(self):
        self.top = None

    def pop(self):
        if self.top is not None:
            item = self.top.val
            self.top = self.top.nxt
            return item
        return None

    def push(self, item):
        t = NodeWithMin(item)
        t.nxt = self.top
        if self.top is not None:
            t.min_val = min(item, self.top.min_val)
        self.top = t

    def min(self):
        return self.top.min_val

class StackWithMin2(Stack):
    def __init__(self):
        super(StackWithMin2, self).__init__()
        self.stack = Stack()

    def pop(self):
        item = super(StackWithMin2, self).pop()
        if item == self.min():
            self.stack.pop()
        return item

    def push(self, item):
        if item <= self.min():
            self.stack.push(item)
        super(StackWithMin2, self).push(item)

    def min(self):
        if self.stack.top is not None:
            return self.stack.top.val
        else:
            return 1e10

def test():
    s1 = StackWithMin()
    s1.push(3)
    s1.push(2)
    s1.push(4)
    print(s1.min())
    s1.pop()
    print(s1.min())
    s1.pop()
    print(s1.min())

    print("=" * 10)

    s2 = StackWithMin2()
    s2.push(3)
    s2.push(2)
    s2.push(4)
    print(s2.min())
    s2.pop()
    print(s2.min())
    s2.pop()
    print(s2.min())

test()
