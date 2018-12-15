### An array A[1...n] contains all the integers from 0 to n except for one number
### which is missing. In this problemm, we cannot access an entire integer in A
### with a single operation. The elements of A are represented in binary, and the
### only operation we can use to access them is "fetch the jth bit of A[i]", which
### takes constant time. Write code to find the missing integer. Can you do it in
### O(n) time?

def findMissng(arr, idx):
    if len(arr) == 0:
        return 0
    even_arr = []
    odd_arr = []
    for x in arr:
        tmp = x & (1 << idx)
        if tmp:
            odd_arr.append(x)
        else:
            even_arr.append(x)
    if len(odd_arr) >= len(even_arr):
        return (findMissng(even_arr, idx + 1) << 1) | 0
    else:
        return (findMissng(odd_arr, idx + 1) << 1) | 1

test_arr = [0, 1, 3, 4, 5]
print(findMissng(test_arr, 0))
