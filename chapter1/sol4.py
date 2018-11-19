### Write a method to decide if two strings are anagrams or not.

def anagram(s, t):
    return sorted(s) == sorted(t)

def test():
    s1 = "listen"
    t1 = "slient"
    print(s1, t1, anagram(s1, t1))

    s2 = "fox"
    t2 = "ox"
    print(s2, t2, anagram(s2, t2))

test()
