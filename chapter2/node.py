### Definition for singly-linked list.

class ListNode:
    def __init__(self, d):
        self.val = d
        self.nxt = None

def appendToTail(head, d):
    end = ListNode(d)
    cur = head
    while cur.nxt is not None:
        cur = cur.nxt
    cur.nxt = end

def deleteNode(head, d):
    cur = head
    if cur.val == d:
        return head.nxt
    while cur.nxt is not None:
        if cur.val == d:
            cur.nxt = cur.nxt.nxt
            return head
        cur = cur.nxt
    print("No node has val: %d" % d)
    return head

def printList(head):
    cur = head
    info = ""
    while cur.nxt is not None:
        info += "%d->" % cur.val
        cur = cur.nxt
    info += "%d" % cur.val
    print(info)

def test():
    n = ListNode(3)
    appendToTail(n, 1)
    appendToTail(n, 4)
    appendToTail(n, 2)
    printList(n)
    n = deleteNode(n, 3)
    printList(n)
    n = deleteNode(n, 4)
    printList(n)
    n = deleteNode(n, 5)
    printList(n)

if __name__ == "__main__":
    test()
