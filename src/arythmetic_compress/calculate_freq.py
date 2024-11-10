from utils.logger import get_logger

logger = get_logger(__name__)


def calculate_frequencies(data: str):
    freq = {}
    for char in data:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    length_string = len(data)

    logger.debug(f"Total characters: {length_string}")
    logger.debug(f"Total unique characters: {len(freq)}")
    logger.debug(f"Unique characters: {freq}")

    # Создаем таблицу частот
    freq_table = {char: f"{count}/{length_string}" for char, count in freq.items()}

    logger.debug(f"Frequency table: {freq_table}")

    return freq_table, freq, length_string
