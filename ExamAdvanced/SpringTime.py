def start_spring(**param):
    elements_dict = {}
    for key, value in param.items():
        if value not in elements_dict.keys():
            elements_dict[value] = [key]
        else:
            if key not in elements_dict.values():
                elements_dict[value].append(key)
    final_print = ""
    for key, value in sorted(elements_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        final_print += f'{key}:\n'
        for sub_value in sorted(value):
            final_print += f'-{sub_value}\n'

    return final_print
