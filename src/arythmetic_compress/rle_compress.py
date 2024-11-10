def rle_compress(data: list) -> list:
    if len(data) <= 0:
        raise ValueError("Массив должен быть не пуст.")

    compressed = []
    count = 1

    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed.append(count)
            compressed.append(data[i - 1])
            count = 1

    compressed.append(count)
    compressed.append(data[-1])

    return compressed
