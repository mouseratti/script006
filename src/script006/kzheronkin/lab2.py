import types


def remove_dublicates_from_list(input_list):
    return list(set(input_list))


def get_str_from_list(input_list):
    str_output = ""
    for sym in input_list:
        str_output += str(sym)


def flatten_nested_list_in_list(input_list):
    res_list = list()
    for el in input_list:
        if isinstance(input_list, list):
            res_list.extend(input_list)
        else:
            res_list += [el]
    return res_list


def map_two_list_in_dict(list_keys, list_values):
    if len(list_keys) != len(list_values):
        raise ValueError
    res_dict = dict(zip(list_keys, list_values))
    return res_dict


def print_a_dict_of_squares(n: int):
    res_dict = {i: i**2 for i in range(1, n+1)}
    return res_dict

