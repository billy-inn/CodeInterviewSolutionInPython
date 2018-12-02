### In the classic problem of the Towers of Hanoi, you have 3 rods and N disks of different
### sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending
### order of size from top to bottom. You have the following constraints:
### (A) Only one disk can be moved at a time.
### (B) A disk is slid off the top of one rod onto the next rod.
### (C) A disk can only be placed on top of a larger disk.
### Write a program to move the disks from the first rod to the last using Stacks.

def move(n, source, target, middle):
    if n == 0:
        return
    move(n - 1, source, middle, target)
    print("Move disk %d from rob %d to rob %d" % (n, source, target))
    move(n - 1, middle, target, source)

def test():
    move(3, 1, 3, 2)

test()
