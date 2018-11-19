### Assume you have a method isSubstring which checks if one word is a substring of
### another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1
### using only one call to isSubstring.

def isSubstring(s, t):
    return t in s

def isRotation(s, t):
    n_s = len(s)
    n_t = len(t)
    if n_s != n_t:
        return False
    if n_s == 0:
        return False

    return isSubstring(s + s, t)

def test():
    s1 = "waterbottle"
    t1 = "erbottlewat"
    print(s1, t1, isRotation(s1, t1))

    s2 = "fox"
    t2 = "ofx"
    print(s2, t2, isRotation(s2, t2))

test()
