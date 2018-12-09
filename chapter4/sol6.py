### Design an algorithm and write code to find the first common ancestor of two nodes
### in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is
### not necessarily a binary search tree.

from utils import TreeNode

def LCA(root, p, q):
    if root is None:
        return None

    if root.val == p:
        return root
    if root.val == q:
        return root

    left_lca = LCA(root.left, p, q)
    right_lca = LCA(root.right, p, q)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca

def test():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print("LCA(4, 5) = ", LCA(root, 4, 5).val)
    print("LCA(4, 6) = ", LCA(root, 4, 6).val)
    print("LCA(3, 4) = ", LCA(root, 3, 4).val)
    print("LCA(2, 4) = ", LCA(root, 2, 4).val)

test()
