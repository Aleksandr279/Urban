def get_matrix_(n, m, value):
    matrix_i = []

    for i in range(n):
        matrix_j = []
        for j in range(m):
            matrix_j.append(value)
        matrix_i.append(matrix_j)

    return matrix_i

result_1 = get_matrix_(2, 2, 10)
result_2 = get_matrix_(3, 5, 42)
result_3 = get_matrix_(4, 2, 13)
print(result_1)
print(result_2)
print(result_3)
