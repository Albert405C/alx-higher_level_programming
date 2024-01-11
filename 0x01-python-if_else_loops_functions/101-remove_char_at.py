def remove_char_at(input_str, n):
    if n < 0 or n >= len(input_str):
        # Check if the index is out of bounds
        print("Index out of bounds.")
        return input_str
    result_str = input_str[:n] + input_str[n+1:]

    return result_str
