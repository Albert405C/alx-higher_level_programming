def element_at(my_list, idx):
    # Check if idx is negative
    if idx < 0:
        return None

    # Check if idx is within the range of the list
    if 0 <= idx < len(my_list):
        return my_list[idx]
    else:
        return None
