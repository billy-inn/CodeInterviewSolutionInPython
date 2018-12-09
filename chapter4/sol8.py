### You are given a binary tree in which each node contains a value. Design an algorithm
### to print all paths which sum up to that value. Note that it can be any path in the
### tree - it does not have to start at the root.

def findSum(head, cnt, buf, level):
    if head is None:
        return
    tmp = cnt
    buf.append(head.val)
    for i in range(level, -1, -1):
        tmp -= buf[i]
        if tmp == 0:
            printList(buf[i:])

    buf1 = [x for x in buf]
    findSum(head.left, cnt, buf1, level + 1)
    buf2 = [x for x in buf]
    findSum(head.right, cnt, buf2, level + 1)

def printList(buf):
    for x in buf[:-1]:
        print(x, "->")
    print(buf[-1])

### call findSum(head, cnt, [], 0)
