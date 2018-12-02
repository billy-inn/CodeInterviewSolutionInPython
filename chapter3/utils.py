### Implementation of Stack and Queue

class ListNode:
    def __init__(self, d):
        self.val = d
        self.nxt = None

def list2str(head):
    cur = head
    info = ""
    while cur.nxt is not None:
        info += "%d->" % cur.val
        cur = cur.nxt
    info += "%d" % cur.val
    return info

class Stack:
    def __init__(self):
        self.top = None

    def __repr__(self):
        return list2str(self.top)

    def pop(self):
        if self.top is not None:
            item = self.top.val
            self.top = self.top.nxt
            return item
        return None

    def push(self, item):
        t = ListNode(item)
        t.nxt = self.top
        self.top = t

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def __repr__(self):
        return list2str(self.first)

    def enqueue(self, item):
        if self.first is None:
            self.last = ListNode(item)
            self.first = self.last
        else:
            self.last.nxt = ListNode(item)
            self.last = self.last.nxt

    def dequeue(self):
        if self.first is not None:
            item = self.first.val
            self.first = self.first.nxt
            return item
        return None


def test():
    s = Stack()
    s.push(3)
    s.push(2)
    print(s)
    print(s.pop())
    print(s)

    q = Queue()
    q.enqueue(1)
    q.enqueue(3)
    print(q)
    print(q.dequeue())
    print(q)

if __name__ == "__main__":
    test()
