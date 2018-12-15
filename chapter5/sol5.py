### Write a function to determine the number of bits required to convert
### integer A to integer B

def bitSwapRequired(a, b):
    cnt = 0
    c = a ^ b
    while c > 0:
        cnt += c & 1
        c >>= 1
    return cnt

print(bitSwapRequired(31, 14))
