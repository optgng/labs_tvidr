from utils.logger import get_logger

logger = get_logger(__name__)


def mtf_encode(input_string: str) -> list:
    symbol_table = list(dict.fromkeys(input_string))
    sorted_symbol_table = sorted(symbol_table)

    logger.debug(f"Sorted symbol table : {sorted_symbol_table}")

    encoded_output = []

    for char in input_string:
        index = sorted_symbol_table.index(char)
        encoded_output.append(index)

        sorted_symbol_table.insert(0, sorted_symbol_table.pop(index))

    logger.debug(f"Encoded output : {encoded_output}")

    return encoded_output
