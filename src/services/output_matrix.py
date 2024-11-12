def print_matrix(matrix: list):
    for row in matrix:
        print(" ".join(f"{elem:3}" for elem in row))
