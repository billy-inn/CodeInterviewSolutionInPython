### Write codde to remove duplicates from an unsorted linked list.
### How would you solve this problem if a temporary buffer is not allowed?

from node import ListNode, appendToTail, printList

def deleteDups(head):
    cur = head
    prev = None
    table = set()
    while cur.nxt is not None:
        if cur.val in table:
            prev.nxt = prev.nxt.nxt
        else:
            table.add(cur.val)
            prev = cur
        cur = cur.nxt

def deleteDupsWithoutBuffer(head):
    prev = head
    cur = prev.nxt
    while cur is not None:
        tmp = head
        while tmp != cur:
            if tmp.val == cur.val:
                prev.nxt = cur.nxt
                cur = prev.nxt
                break
            tmp = tmp.nxt
        if tmp == cur:
            prev = cur
            cur = cur.nxt

def test():
    n = ListNode(3)
    appendToTail(n, 1)
    appendToTail(n, 4)
    appendToTail(n, 2)
    appendToTail(n, 3)
    appendToTail(n, 3)
    appendToTail(n, 2)
    printList(n)
    deleteDupsWithoutBuffer(n)
    printList(n)

test()
