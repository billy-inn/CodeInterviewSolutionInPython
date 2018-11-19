### Implement an algorithm to determine if a string has all unique characters
### What if you can not use additional data structures?

def isUniqueChars(s):
    checker = 0
    for c in s:
        val = ord(c) - ord('a')
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
    return True

def test():
    test1 = 'abcdefz'
    print(test1, isUniqueChars(test1))
    test2 = 'cdfeezz'
    print(test2, isUniqueChars(test2))

test()
