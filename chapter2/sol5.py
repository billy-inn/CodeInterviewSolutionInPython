### Given a circular linked list, implement an algorithm which returns node
### at the beginning of the loop.

from node import ListNode

def findBeginning(head):
    n1 = head
    n2 = head

    while n2.nxt is not None:
        n1 = n1.nxt
        n2 = n2.nxt.nxt
        if n1 == n2:
            break

    if n2.nxt is None:
        print("no loop!")
        return None

    n1 = head
    while n1 != n2:
        n1 = n1.nxt
        n2 = n2.nxt
    return n2

def test():
    a = ListNode('A')
    b = ListNode('B')
    c = ListNode('C')
    d = ListNode('D')
    e = ListNode('E')
    a.nxt = b
    b.nxt = c
    c.nxt = d
    d.nxt = e
    e.nxt = c
    print(findBeginning(a).val)

test()
