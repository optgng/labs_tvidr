def print_array(array: list):
    if not array:
        print("Массив пуст.")
        return

    max_width = max(len(str(elem)) for elem in array)

    formatted_array = " ".join(f"{elem:>{max_width}}" for elem in array)

    print(formatted_array)
