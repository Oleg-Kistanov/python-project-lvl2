#!/usr/bin/env python3

import json


def generate_diff(file_path1, file_path2):
    file_1 = json.load(open(file_path1))
    file_2 = json.load(open(file_path2))
    old_keys = list(file_1.keys())
    new_keys = list(file_2.keys())
    shared_keys = sorted(list(set(old_keys + new_keys)))
    list_of_strings = []

    for key in shared_keys:
        if key not in file_2:
            string = "- {}: {}".format(key, str(file_1.get(key)))
            list_of_strings.append(string)
        elif key not in file_1:
            string = "+ {}: {}".format(key, str(file_2.get(key)))
            list_of_strings.append(string)
        elif file_1[key] == file_2[key]:
            string = "  {}: {}".format(key, str(file_1.get(key)))
            list_of_strings.append(string)
        else:
            string = "- {}: {}".format(key, str(file_1.get(key)))
            list_of_strings.append(string)
            string = "+ {}: {}".format(key, str(file_2.get(key)))
            list_of_strings.append(string)

    result = "{\n\t" + "\n\t".join(list_of_strings) + "\n}"
    return result
