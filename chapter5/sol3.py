### Given an integer, print the next smallest and next largest number that
### have the same number of 1 bits in their binary representation.

def get_bit(n, idx):
    return (n & (1 << idx)) > 0

def set_bit(n, idx, flag):
    if flag:
        return n | (1 << idx)
    else:
        mask = ~(1 << idx)
        return n & mask

def get_next(n):
    if n <= 0:
        return -1
    idx = 0
    cnt_ones = 0
    while not get_bit(n, idx):
        idx += 1

    while get_bit(n, idx):
        idx += 1
        cnt_ones += 1
    n = set_bit(n, idx, True)

    idx -= 1
    n = set_bit(n, idx, False)
    cnt_ones -= 1

    for i in range(idx - 1, cnt_ones - 1, -1):
        n = set_bit(n, i, False)

    for i in range(cnt_ones):
        n = set_bit(n, i, True)

    return n

def get_prev(n):
    if n <= 0:
        return -1
    idx = 0
    cnt_zeros = 0
    while get_bit(n, idx):
        idx += 1

    while not get_bit(n, idx):
        idx += 1
        cnt_zeros += 1
    n = set_bit(n, idx, False)

    idx -= 1
    n = set_bit(n, idx, True)
    cnt_zeros -= 1

    for i in range(idx - 1, cnt_zeros - 1, -1):
        n = set_bit(n, i, True)

    for i in range(cnt_zeros):
        n = set_bit(n, i, False)

    return n

def test():
    print(bin(5))
    print(bin(get_next(5)))
    print(bin(get_prev(5)))

test()
