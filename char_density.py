from assets import chars_list, density_list

# temp_lst = (chars_list.chars, density_list.density)
char_density_dct = {
    key: value for key, value in zip(chars_list.chars, density_list.density)
}


def char_density_sort(string, dict=char_density_dct):

    ordered_lst = []
    ordered_string = ""
    string_set = set(string)
    string_unique = "".join(string_set)
    for c in string_unique:
        for key in dict.keys():
            if key == c:
                ordered_lst.append(dict[key])
    ordered_lst.sort()
    for c in ordered_lst:
        for key, value in dict.items():
            if c == value:
                ordered_string += key
    return ordered_string
