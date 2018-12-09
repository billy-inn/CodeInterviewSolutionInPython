### You have two very large binary trees: T1, with millions of nodes, and T2, with
### hundreds of nodes. Create an algorithm to decide if T2 is a subtree of T1.

def containsTree(t1, t2):
    if t2 is None:
        return True
    return subtree(t1, t2)

def subtree(t1, t2):
    if t1 is None:
        return False
    if t1.val == t2.val:
        if match(t1, t2):
            return True
    return subtree(t1.left, t2) or subtree(t1.right, t2)

def match(t1, t2):
    if (t1 is None) and (t2 is None):
        return True
    if (t1 is None) or (t2 is None):
        return False
    if t1.val != t2.val:
        return False
    return match(t1.left, t2.left) and match(t1.right, t2.right)
