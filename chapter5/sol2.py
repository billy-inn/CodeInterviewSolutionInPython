### Given a (decimal - e.g. 3.72) number that is passed in as a string, print the binary
### representation. If the number can not be represented accurately in binary, print "ERROR"

def printBinary(s):
    intPart, decPart = s.split('.')
    intPart = int(intPart)
    decPart = float(s) - intPart
    int_str = ""
    while intPart > 0:
        r = intPart % 2
        intPart >>= 1
        int_str = str(r) + int_str
    dec_str = ""
    while decPart > 0:
        if len(dec_str) > 32:
            return "ERROR"
        if decPart == 1:
            dec_str += "1"
            break
        r = decPart * 2
        if r >= 1:
            dec_str += "1"
            decPart = r - 1
        else:
            dec_str += "0"
            decPart = r
    return int_str + "." + dec_str

def test():
    print(printBinary("3.5"))
    print(printBinary("0.25"))
    print(printBinary("4.625"))
    print(printBinary("3.72"))


test()
