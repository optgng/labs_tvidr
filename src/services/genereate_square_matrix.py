import random


def generate_square_matrix(size: int):
    if size <= 0:
        raise ValueError("Размер матрицы должен быть больше нуля.")

    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(i * size + j + 1)
        matrix.append(row)

    return matrix


def generate_square_matrix_random(n: int, min_value: int = 0, max_value: int = 4) -> list:
    matrix = []

    for i in range(n):
        row = [random.randint(min_value, max_value) for _ in range(n)]
        matrix.append(row)

    return matrix

