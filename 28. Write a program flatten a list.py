def flatten_nested_list(list1):
    flattened_list = []
    for i in list1:
        if isinstance(i, list):
            flattened_list.extend(flatten_nested_list(i))
        else:
            flattened_list.append(i)
    return flattened_list
nested_list = [7, [2, 3], 4, [2, [3, 4], 5], 6, [7, 8]]
result = flatten_nested_list(nested_list)
print("Flattened list : ", result)