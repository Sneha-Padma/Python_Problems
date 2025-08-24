# Day9 Matrix Multiplication
def matrix_multiplication():
    p, q, r = map(int, input().split())
    matrix_a = []
    for _ in range(p):
        matrix_a.append(list(map(int, input().split())))

    matrix_b = []
    for _ in range(q):
        matrix_b.append(list(map(int, input().split())))

    matrix_c = [[0 for _ in range(r)] for _ in range(p)]

    for i in range(p):
        for j in range(r):
            for k in range(q):
                matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]

    for row in matrix_c:
        print(*row)
matrix_multiplication()