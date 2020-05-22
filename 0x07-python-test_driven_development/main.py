#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

print(lazy_matrix_mul([[0, 0], [1, 1]], [[2, 2], [4, 4]]))
print(lazy_matrix_mul([[1, 1]], [[4, 4], [5, 5]]))
print(lazy_matrix_mul([[0.5, -1]], [[1.5, -4], [5, 5]]))

try:
    print(lazy_matrix_mul("abc", [[1, 1], [2, 2]])
except Exception as e:
    print(e)

try:
    print(lazy_matrix_mul([1, "a"], [[1, 1], [2, 2]])
except Exception as e:
    print(e)

try:
    print(lazy_matrix_mul([], [[1, 1], [2, 2]])
except Exception as e:
    print(e)

try:
    print(lazy_matrix_mul([[1, 1, 1], [2, 2, 2]], [[3, 3], [4, 4]])
except Exception as e:
    print(e)
