class Matrix:
    '''
    Класс Matrix для создания матриц и произведения
    математический операций с ними
    '''
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        """Вывод матрицы на печать"""
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        """Сравнение матриц между собой"""
        return self.matrix == other.matrix

    def __add__(self, other):
        """Сложение матриц"""
        if (len(self.matrix[0])) != len(other.matrix):
            print("Количество строк и колонок матриц не совпадают")
            return -1
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                       for i in range(len(self.matrix))])

    def __mul__(self, other):
        """Умножение матриц"""
        if (len(self.matrix[0])) != len(other.matrix):
            print("Количество строк и колонок матриц не совпадают")
            return -1
        return Matrix([[sum([self.matrix[i][k] * other.matrix[k][j] for k in range(len(other.matrix))])
                        for j in range(len(other.matrix[0]))] for i in range(len(self.matrix))])


m1 = Matrix(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)

m2 = Matrix(
    [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
)

m3 = Matrix(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)

m4 = Matrix(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
)
if __name__ == '__main__':
    print(f"m1 = m3: {m1 == m3}")
    print(f"{m1}\n{m4}\n")
    print(m1 * m4)
