### Design an algorithm and write code to remove the duplicate characters in a string
### without using any additional buffer.

def removeDuplicates(s):
    n = len(s)
    if n < 2:
        return s

    hit = [False for _ in range(256)]
    res = ''
    for i in range(n):
        c = s[i]
        if not hit[ord(c)]:
            hit[ord(c)] = True
            res += c

    return res

def test():
    test1 = 'abcd'
    print(test1, removeDuplicates(test1))
    test2 = 'aaaa'
    print(test2, removeDuplicates(test2))
    test3 = ''
    print(test3, removeDuplicates(test3))
    test4 = 'aaabbb'
    print(test4, removeDuplicates(test4))
    test5 = 'abababa'
    print(test5, removeDuplicates(test5))

test()
