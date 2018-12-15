### You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write
### a method to set all bits between i and j in N equal to M.

def updateBits(n, m, i, j):
    tmp = (1 << (j + 1)) - (1 << i)
    n -= (n & tmp)
    n |= (m << i)
    return n

def updateBits2(n, m, i, j):
    tmp = (1 << 32) - 1
    left = tmp - ((1 << j) - 1)
    right = (1 << i) - 1
    mask = left | right
    return (n & mask) | (m << i)

def test():
    n = 1 << 10
    m = 21
    print("n:", bin(n))
    print("m:", bin(m))
    print(bin(updateBits(n, m, 2, 6)))
    print(bin(updateBits2(n, m, 2, 6)))


test()
