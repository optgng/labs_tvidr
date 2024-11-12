from utils.logger import get_logger

logger = get_logger(__name__)


def mtf_decode(encoded_indices: list, original_string: str) -> str:
    symbol_table = list(dict.fromkeys(original_string))
    sorted_symbol_table = sorted(symbol_table)

    logger.debug(f"Sorted symbol table : {sorted_symbol_table}")

    decoded_output = []

    for index in encoded_indices:
        char = sorted_symbol_table[index]
        decoded_output.append(char)

        sorted_symbol_table.insert(0, sorted_symbol_table.pop(index))

    logger.debug(f"Encoded output : {''.join(decoded_output)}")

    return ''.join(decoded_output)
