### Implement an algorithm to find the nth to last element of a singly linked list.

from node import ListNode, appendToTail, printList

def nthToLast(head, n):
    if (head is None) or (n < 1):
        return None
    cur1 = head
    cur2 = head
    for _ in range(n - 1):
        if cur1 is None:
            return None
        cur1 = cur1.nxt
    while cur1.nxt is not None:
        cur1 = cur1.nxt
        cur2 = cur2.nxt
    return cur2.val

def test():
    n = ListNode(3)
    appendToTail(n, 1)
    appendToTail(n, 4)
    appendToTail(n, 2)
    appendToTail(n, 3)
    appendToTail(n, 3)
    appendToTail(n, 2)
    printList(n)
    print("4th to last:", nthToLast(n, 4))
    print("6th to last:", nthToLast(n, 6))

test()
