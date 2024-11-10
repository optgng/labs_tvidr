from utils.logger import get_logger
from arythmetic_compress.calculate_freq import calculate_frequencies
from arythmetic_compress.calculate_cumulative_freq import calculate_cumulative_freq
from arythmetic_compress.arythmetic_encode import arithmetic_encode
from arythmetic_compress.arythmetic_decode import arithmetic_decoding

logger = get_logger(__name__)


if __name__ == "__main__":
    test_string = ("Потом они заговорили о чем-то другом, и вскоре пришла пора Пуху и Пятачку идти домой. Они пошли "
                   "вместе. Сперва, пока они плелись по тропинке на краю Дремучего Леса, оба молчали; но когда они "
                   "дошли до речки и стали помогать друг другу перебираться по камушкам, а потом бок о бок пошли по "
                   "узкой тропке между кустов, у них завязался Очень Умный Разговор")
    logger.info("Тестовая строка: " + test_string)

    freq_table, freq, length_string = calculate_frequencies(test_string)

    print("\n" + "#"*80)
    logger.info("Таблица частот: " + str(freq_table))
    logger.info("Частота: " + str(freq))
    logger.info("Общее количество символов: " + str(length_string))

    working_segment = calculate_cumulative_freq(freq, length_string)

    print("\n" + "#"*80)
    logger.info("Рабочий сегмент: " + str(working_segment))

    print("\n" + "#"*80)
    encoded_value = arithmetic_encode(test_string, freq, working_segment, length_string)
    logger.info("Закодированное значение: " + str(encoded_value))

    # decoded_string = arithmetic_decoding(encoded_value, length_string, freq, working_segment)
    #
    # print("\n" + "#"*80)
    # logger.info("Раскодированное значение: " + str(decoded_string))

