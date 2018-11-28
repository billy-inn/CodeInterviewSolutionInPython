### Implement an algorithm to delete a node in the middle of a single linked list,
### given only access to that node.

from node import ListNode, appendToTail, printList

def deleteNode(node):
    if (node is None) or (node.nxt is None):
        return False
    nxt = node.nxt
    node.val = nxt.val
    node.nxt = nxt.nxt
    return True

def test():
    n = ListNode(3)
    appendToTail(n, 1)
    appendToTail(n, 4)
    appendToTail(n, 2)
    appendToTail(n, 3)
    appendToTail(n, 3)
    appendToTail(n, 2)
    printList(n)
    deleteNode(n)
    printList(n)

test()
