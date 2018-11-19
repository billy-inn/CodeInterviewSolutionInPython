### Given an image represented by an NxN matrix, where each pixel in the image is 4
### bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

def rotate(mat):
    n = len(mat)
    for i in range(n // 2):
        first = i
        last = n - i - 1
        for j in range(n - 2 * i - 1):
            tmp = mat[first][first + j]
            mat[first][first + j] = mat[last - j][first]
            mat[last - j][first] = mat[last][last - j]
            mat[last][last - j] = mat[first + j][last]
            mat[first + j][last] = tmp
    return mat

def print_mat(mat):
    for row in mat:
        print(row)

def test():
    mat1 = [[1, 2], [3, 4]]
    print_mat(mat1)
    print("-" * 20)
    print_mat(rotate(mat1))

    print("=" * 20)

    mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_mat(mat2)
    print("-" * 20)
    print_mat(rotate(mat2))

test()
