### Given a sorted (increasing order) array, write an algorithm to create a binary tree
### with minimal height.

from utils import TreeNode

def addToTree(arr, start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    n = TreeNode(arr[mid])
    n.left = addToTree(arr, start, mid - 1)
    n.right = addToTree(arr, mid + 1, end)
    return n

def createMinimalBST(arr):
    return addToTree(arr, 0, len(arr) - 1)
