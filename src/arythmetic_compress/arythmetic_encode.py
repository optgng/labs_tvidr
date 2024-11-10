from utils.logger import get_logger

logger = get_logger(__name__)


def arithmetic_encode(data: str, freq: dict, cumulative_freq: dict, length_string: int) -> float:
    low_interval = 0.0
    high_interval = 1.0

    for char in data:
        range_width = high_interval - low_interval
        high_interval = low_interval + range_width * cumulative_freq[char]
        low_interval = low_interval + range_width * (cumulative_freq[char] - (freq[char] / length_string))

        logger.debug(f"Encoding '{char}': interval=({round(low_interval, 4)}, {round(high_interval, 4)})")

    encoded_value = (low_interval + high_interval) / 2
    logger.debug(f"Encoded value: {encoded_value}")

    return encoded_value
