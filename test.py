def split_dict(input_dict: dict, num_parts: int) -> list:
    list_len: int = len(input_dict)
    return [dict(list(input_dict.items())[i * list_len // num_parts:(i + 1) * list_len // num_parts])
        for i in range(num_parts)]

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(split_dict(d, 3))
print(split_dict(d, 7))