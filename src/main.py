from utils.logger import get_logger
from arythmetic_compress.calculate_freq import calculate_frequencies
from arythmetic_compress.calculate_cumulative_freq import calculate_cumulative_freq
from arythmetic_compress.arythmetic_encode import arithmetic_encode
from arythmetic_compress.arythmetic_decode import arithmetic_decoding
from bwt_compress.bwt_encode import bwt_encode
from bwt_compress.bwt_decode import bwt_decode
from mtf_compress.mtf_encode import mtf_encode
from mtf_compress.mtf_decode import mtf_decode

logger = get_logger(__name__)

if __name__ == "__main__":
    test_string = ("Потом они заговорили о чем-то другом, и вскоре пришла пора Пуху и Пятачку идти домой. Они пошли "
                   "вместе. Сперва, пока они плелись по тропинке на краю Дремучего Леса, оба молчали; но когда они "
                   "дошли до речки и стали помогать друг другу перебираться по камушкам, а потом бок о бок пошли по "
                   "узкой тропке между кустов, у них завязался Очень Умный Разговор")
    logger.info("Тестовая строка: " + test_string)

    freq_table, freq, length_string = calculate_frequencies(test_string)

    print("\n" + "#" * 80)
    logger.info("Таблица частот: " + str(freq_table))
    logger.info("Частота: " + str(freq))
    logger.info("Общее количество символов: " + str(length_string))

    working_segment = calculate_cumulative_freq(freq, length_string)

    print("\n" + "#" * 80)
    logger.info("Рабочий сегмент: " + str(working_segment))

    print("\n" + "#" * 80)
    encoded_value = arithmetic_encode(test_string, freq, working_segment, length_string)
    logger.info("Закодированное значение: " + str(encoded_value))

    print("\n" + "#" * 80)
    bwt_string = "КЕНРПАУКАРЕКРЛАО"
    logger.info("Исходная строка BWT: " + bwt_string)

    encoded_bwt_string, original_index = bwt_encode(bwt_string)
    logger.info("Закодированная строка BWT: " + encoded_bwt_string)

    print("\n" + "#" * 80)
    logger.info("Исходная строка MTF: " + encoded_bwt_string)

    encoded_mtf_string = mtf_encode(encoded_bwt_string)
    logger.info("Закодированная строка MTF: " + ''.join(str(num) for num in encoded_mtf_string))

    print("\n" + "#" * 80)
    decoded_mtf_string = mtf_decode(encoded_mtf_string, encoded_bwt_string)
    logger.info("Декодированная строка MTF: " + decoded_mtf_string)
    decoded_bwt_string = bwt_decode(decoded_mtf_string, original_index)
    logger.info("Декодированная строка BWT: " + decoded_bwt_string)
    assert (decoded_bwt_string == bwt_string)
