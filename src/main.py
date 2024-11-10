from services.output_matrix import print_matrix
from services.output_array import print_array
from services.genereate_square_matrix import generate_square_matrix
from services.genereate_square_matrix import generate_square_matrix_random
from services.save_output_to_file import save_output_to_file
from core.column_traversal import column_traversal
from core.rle_compress import rle_compress
from core.hufmann_compress import huffman_compress
from utils.logger import get_logger

logger = get_logger(__name__)


def output(matrix: list, matrix_size: int, depth: int):
    print("\n" + "#" * 80)
    print("Исходная матрица:")
    print_matrix(matrix)

    traversal_result = column_traversal(matrix, matrix_size, depth)

    print("\n" + "#" * 80)
    print("Результат обхода:")
    print_array(traversal_result)

    print("\n" + "#" * 80)
    print("Результат RLE сжатия:")
    rle_result = rle_compress(traversal_result)
    print_array(rle_result)

    print("\n" + "#" * 80)
    huffman_codes, compressed_data = huffman_compress(rle_result)

    print("Словарь Хаффмана:")
    print(huffman_codes)

    print("\n")
    print("Результат сжатия:")
    print_array(compressed_data)

    print("\n")


if __name__ == "__main__":
    matrix_size = int(input("Введите размерность матрицы: "))

    depth = int(input("Введите глубину обхода(depth): "))

    logger.info("Создаю матрицу...")
    matrix = generate_square_matrix_random(matrix_size)

    output(matrix, matrix_size, depth)
    logger.info("Сохраняю вывод в файл...")
    save_output_to_file("data/output.txt", output, matrix, matrix_size, depth)


