from utils.logger import get_logger

logger = get_logger(__name__)


def bwt_decode(last_column, original_index):
    n = len(last_column)

    first_column = sorted(last_column)

    logger.debug("First column: {}".format(first_column))

    lf_mapping = sorted((char, i) for i, char in enumerate(last_column))

    logger.debug("lf_mapping: {}".format(lf_mapping))

    output = []
    index = original_index

    for _ in range(n):
        output.append(last_column[index])
        index = next(
            i for i, (char, _) in enumerate(lf_mapping) if char == last_column[index] and lf_mapping[i][1] == index)

    return ''.join(reversed(output))
