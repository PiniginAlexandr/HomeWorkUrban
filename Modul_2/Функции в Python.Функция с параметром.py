def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        low_l = []
        matrix.append(low_l)
        for k in range(m):
            low_l.append(value)

    return matrix
print(get_matrix(2, 2, 10))
print(get_matrix(3, 5, 42))
print(get_matrix(4, 2, 13))

# Вывод на консоль:
# [[10, 10], [10, 10]]
# [[42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42]]
# [[13, 13], [13, 13], [13, 13], [13, 13]]

