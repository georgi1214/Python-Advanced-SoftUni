def naughty_or_nice_list(tuples_names, *arguments, **keywords):
    not_found = []
    found_kids = {'Nice': [], "Naughty": []}
    names_dict = {}
    for number, name in tuples_names:
        if number not in names_dict:
            names_dict[number] = []
        names_dict[number].append(name)

    arguments_dict = {}
    if arguments:
        for el in arguments:
            command = int(el[0])
            behavior = el[2:]
            arguments_dict[command] = behavior

    for command, behavior in arguments_dict.items():
        if command in names_dict.keys() and not len(names_dict[command]) > 1:
            found_kids[behavior].extend(names_dict[command])
            del names_dict[command]
    repeating_names = 0
    if keywords:
        for name, behavior in keywords.items():
            for el_list in names_dict.values():
                if name in el_list:
                    repeating_names += el_list.count(name)
                    if not repeating_names > 1:
                        found_kids[behavior].extend([name])
                        repeating_names = 0
                        for key, values in names_dict.items():
                            if name in values:
                                names_dict[key].remove(name)
                                continue

    for key, last_value in names_dict.items():
        if last_value:
            not_found.extend(last_value)
            names_dict[key] = []

    final_print = ""
    for behave, names in found_kids.items():
        if names:
            final_print += f"{behave}: {', '.join(names)}\n"
    last_names = []
    if not_found:
        final_print += f'Not found: '
        for name in not_found:
            last_names.append(name)
    final_print += f'{", ".join(last_names)}'

    return final_print