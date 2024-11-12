from utils.logger import get_logger

logger = get_logger(__name__)


def bwt_encode(input_string: str) -> tuple[str, int]:
    n = len(input_string)
    rotations = [input_string[i:] + input_string[:i] for i in range(n)]

    logger.debug(f'n: {n}')
    logger.debug(f'rotations: {rotations}')

    rotations.sort()

    logger.debug(f'rotations sorted: {rotations}')

    last_column = ''.join(rotation[-1] for rotation in rotations)
    original_index = rotations.index(input_string)

    return last_column, original_index
