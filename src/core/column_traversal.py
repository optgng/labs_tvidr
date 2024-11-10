
def column_traversal(matrix: list, matrix_size: int, depth: int) -> list:
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Матрица должна быть представлена списком списков.")

    if not isinstance(matrix_size, int) or not isinstance(depth, int):
        raise TypeError("Размер матрицы и глубина должны быть int")

    if matrix_size <= 0:
        raise ValueError("Размер матрицы должен быть больше нуля.")

    if depth <= 0:
        raise ValueError("Глубина обхода должна быть больше нуля.")

    if len(matrix) != matrix_size or any(len(row) != matrix_size for row in matrix):
        raise ValueError("Mатрица должна быть квадратной.")

    matrix_processed: list = []
    result: list = []

    # Обход матрицы по столбцам с переворотом
    for i in range(0, matrix_size, depth):
        for col in range(matrix_size):
            temp_array: list = []
            for row in range(0 + i, min(i + depth, matrix_size)):
                temp_array.append(matrix[row][col])
            if col % 2 != 0:
                temp_array = temp_array[::-1]
            matrix_processed.append(temp_array)

    # Преобразование из матрицы в массив
    for row in matrix_processed:
        for elem in row:
            result.append(elem)

    return result
