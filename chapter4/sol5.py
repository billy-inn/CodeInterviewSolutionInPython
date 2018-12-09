### Write an algorithm to find the 'next' node (e.g., in-order successor) of a given node
### in a binary search tree where each node has a link to its parent.

def inOrderSucc(e):
    if e is None:
        return None
    if e.right is not None:
        return leftMostChild(e.right)
    p = e.parent
    while p is not None:
        if p.left == e:
            break
        e = p
        p = e.parent
    return p

def leftMostChild(e):
    if e is None:
        return None
    while e.left is not None:
        e = e.left
    return e
