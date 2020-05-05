#!/usr/bin/python3
if __name__ != "__main__":
    def print_matrix_integer(matrix=[[]]):
        y = len(matrix[0])
        x = len(matrix)
        if y == 0:
            print()
            return
        i = 0
        while i < x:
            j = 0
            while j < y:
                if j != y - 1:
                    print("{}".format(matrix[i][j]), end=' ')
                else:
                    print("{}".format(matrix[i][j]))
                j += 1
            i += 1
