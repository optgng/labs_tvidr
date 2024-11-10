def calculate_probabilities(data: str):
    freq = {}
    for char in data:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    total_chars = len(data)
    print(f"Total characters: {total_chars}")
    print(f"Total unique characters: {len(freq)}")
    print(f"Unique characters: {freq}")

    # Создаем таблицу частот
    freq_table = {char: f"{count}/{total_chars}" for char, count in freq.items()}

    print(f"Frequency table: {freq_table}")

    print(type(freq_table.keys()))


    # Составляем рабочий отрезок
    cumulative_frequency = 0
    working_segment = {}

    sorted_keys = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

    print(f"Sorted keys: {sorted_keys}")
    for char in sorted_keys.keys():
        cumulative_frequency += freq[char]
        working_segment[char] = f"{cumulative_frequency}/{total_chars}"

    print(f"Cumulative frequency: {cumulative_frequency}")
    print(f"Working segment: {working_segment}")


if __name__ == "__main__":
    test_string = "Кох-и-ноор_"
    calculate_probabilities(test_string)
