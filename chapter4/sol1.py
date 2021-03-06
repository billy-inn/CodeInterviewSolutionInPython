### Implement a function to check if a tree is balanced. For the purposes of this question,
### a balanced tree is defined to be a tree such that no two leaf nodes differ in distance
### from the root by more than one.

def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def min_depth(root):
    if root is None:
        return 0
    return 1 + min(min_depth(root.left), min_depth(root.right))

def is_balanced(root):
    return max_depth(root) - min_depth(root) <= 1
