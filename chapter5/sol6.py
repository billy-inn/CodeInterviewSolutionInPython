### Write a program to swap odd and even bits in an integer with as few
### instructions as possible

def swapOddEventBits(x):
    return ((x & 0xaaaaaaaa) >> 1) | ((x & 0x55555555) << 1)

print(bin(1931))
print(bin(swapOddEventBits(1931)))
