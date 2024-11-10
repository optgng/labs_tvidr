from utils.logger import get_logger

logger = get_logger(__name__)


def calculate_cumulative_freq(freq: dict, length_string: int) -> dict:
    cumulative_frequency = 0
    working_freq_segment = {}
    working_number_segment = {}

    sorted_keys = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    
    logger.debug(f"Sorted keys: {sorted_keys}")

    for char in sorted_keys.keys():
        cumulative_frequency += freq[char]
        working_freq_segment[char] = f"{cumulative_frequency}/{length_string}"
        working_number_segment[char] = cumulative_frequency/length_string
    
    logger.debug(f"Cumulative frequency: {cumulative_frequency}")
    logger.debug(f"Working segment: {working_freq_segment}")
    logger.debug(f"Working number segment: {working_number_segment}")

    return working_number_segment
