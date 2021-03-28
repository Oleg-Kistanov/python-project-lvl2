#!/usr/bin/env python3

import json


def generate_diff(file_path1, file_path2):
    file_1 = json.load(open(file_path1))
    file_2 = json.load(open(file_path2))
    old_keys = list(file_1.keys())
    new_keys = list(file_2.keys())
    shared_keys = sorted(list(set(old_keys + new_keys)))
    result = "{\n"

    for key in shared_keys:
        if key not in file_2:
            result += "\t- " + key + ": " + str(file_1[key]) + "\n"
        elif key not in file_1:
            result += "\t+ " + key + ": " + str(file_2[key]) + "\n"
        elif file_1[key] == file_2[key]:
            result += "\t  " + key + ": " + str(file_1[key]) + "\n"
        else:
            result += "\t- " + key + ": " + str(file_1[key]) + "\n"
            result += "\t+ " + key + ": " + str(file_2[key]) + "\n"

    result += "}"
    return result
