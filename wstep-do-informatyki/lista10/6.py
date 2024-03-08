def print_reversed_list(item):
    if item is None:
        return
    print_reversed_list(item.next)
    print(item.value)