### You have two numbers represented by a linked list, where each node contains a signle digit.
### The digits are stored in reverse order, such that the 1's digit is at the head of the list.
### Write a function that adds the two numbers and returns the sum as a linked list.

from node import ListNode, appendToTail, printList

def addLists(n1, n2):
    if (n1 is None) or (n2 is None):
        return None
    head = ListNode(0)
    cur = head
    prev = None
    carry = 0
    while (n1 is not None) or (n2 is not None):
        val = carry
        if n1 is not None:
            val += n1.val
            n1 = n1.nxt
        if n2 is not None:
            val += n2.val
            n2 = n2.nxt
        cur.val = val % 10
        carry = val // 10
        cur.nxt = ListNode(0)
        prev = cur
        cur = cur.nxt
    if carry:
        cur.val = carry
    else:
        prev.nxt = None
    return head

def test():
    n1 = ListNode(3)
    appendToTail(n1, 1)
    appendToTail(n1, 7)
    n2 = ListNode(5)
    appendToTail(n2, 9)
    appendToTail(n2, 2)
    printList(n1)
    printList(n2)
    s = addLists(n1, n2)
    printList(s)

test()
