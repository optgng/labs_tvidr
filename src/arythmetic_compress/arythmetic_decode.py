from utils.logger import get_logger

logger = get_logger(__name__)


def arithmetic_decoding(encoded_value: float, length_string: int, freq: dict, cumulative_freq: dict) -> str:
    decoded_string = []
    low = 0.0
    high = 1.0

    for _ in range(length_string):
        range_width = high - low
        value = (encoded_value - low) / range_width  # Нормализуем закодированное значение

        # Находим символ по нормализованному значению
        for char, cum_freq in cumulative_freq.items():
            if value < cum_freq:
                decoded_string.append(char)
                high = low + range_width * cum_freq
                low = low + range_width * (cumulative_freq[char] - freq[char] / length_string)
                break

        logger.debug(f"Decoded char '{decoded_string[-1]}': low={low}, high={high}")

    return ''.join(decoded_string)
