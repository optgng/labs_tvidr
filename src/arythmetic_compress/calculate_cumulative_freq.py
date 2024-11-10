from utils.logger import get_logger

logger = get_logger(__name__)


def calculate_cumulative_freq(freq: dict, total_chars) -> dict:
    cumulative_frequency = 0
    working_segment = {}
    
    sorted_keys = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    
    logger.debug(f"Sorted keys: {sorted_keys}")

    for char in sorted_keys.keys():
        cumulative_frequency += freq[char]
        working_segment[char] = f"{cumulative_frequency}/{total_chars}"
    
    logger.debug(f"Cumulative frequency: {cumulative_frequency}")
    logger.debug(f"Working segment: {working_segment}")

    return working_segment
