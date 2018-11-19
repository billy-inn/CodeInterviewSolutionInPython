### Write an algorithm uch that if an element in an MxN matrix is 0, its entire row and
### column is set to 0.

def setZeros(mat):
    n = len(mat)

    rows = [False for _ in range(n)]
    cols = [False for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 0:
                rows[i] = True
                cols[j] = True
    for i in range(n):
        for j in range(n):
            if rows[i] or cols[j]:
                mat[i][j] = 0
    return mat

def print_mat(mat):
    for row in mat:
        print(row)

def test():
    mat1 = [[1, 2], [3, 4]]
    print_mat(mat1)
    print("-" * 20)
    print_mat(setZeros(mat1))

    print("=" * 20)

    mat2 = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    print_mat(mat2)
    print("-" * 20)
    print_mat(setZeros(mat2))

    print("=" * 20)

    mat3 = [[1, 2, 3], [0, 5, 6], [7, 8, 0]]
    print_mat(mat3)
    print("-" * 20)
    print_mat(setZeros(mat3))

test()
