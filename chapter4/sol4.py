### Given a binary search tree, design an algorithm which creates a linked list of
### all the nodes at each depth.

def findLevelLinkList(root):
    level = 0
    result = []
    cur_list = [root]
    result.append(cur_list)
    while True:
        cur_list = []
        for n in result[level]:
            if n is not None:
                if n.left is not None:
                    cur_list.append(n.left)
                if n.right is not None:
                    cur_list.append(n.right)
        if len(cur_list) == 0:
            break
        result.append(cur_list)
        level += 1
    return result
