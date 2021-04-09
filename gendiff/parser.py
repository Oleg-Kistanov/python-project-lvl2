#!/usr/bin/env python3

import json
import yaml
import os


def is_json(path):
    extension = os.path.splitext(path)[1].lower()
    if extension == ".json":
        return True
    return False


def is_yml(path):
    extension = os.path.splitext(path)[1].lower()
    if extension == ".yml" or extension == ".yaml":
        return True
    return False


def load_json(path):
    with open(path) as f:
        file = json.load(f)
    return file


def load_yml(path):
    with open(path) as f:
        file = yaml.safe_load(f)
    return file


def parser(path_1, path_2):
    if is_json(path_1) and is_json(path_2):
        file_1 = load_json(path_1)
        file_2 = load_json(path_2)
        return file_1, file_2
    elif is_yml(path_1) and is_yml(path_2):
        file_1 = load_yml(path_1)
        file_2 = load_yml(path_2)
        return file_1, file_2
