#!/usr/bin/env python3

import pytest
from gendiff.parser import *


@pytest.mark.parametrize("path, expected", [
    ("tests/fixtures/before.json", True),
    ("tests/fixtures/before.yaml", False)
] )
def test_is_json(path, expected):
    assert is_json(path) == expected


@pytest.mark.parametrize("path, expected", [
    ("tests/fixtures/before.json", False),
    ("tests/fixtures/before.yaml", True),
    ("tests/fixtures/after.yml", True)
])
def test_is_yml(path, expected):
    assert is_yml(path) == expected


def test_load_json():
    path = "tests/fixtures/before.json"
    data = load_json(path)
    with open("tests/fixtures/before_dict.txt", "r") as f:
        expected = f.read().strip("\n")
    assert f"{data}" == expected


def test_load_yml():
    path = "tests/fixtures/before.yaml"
    data = load_yml(path)
    with open("tests/fixtures/before_dict.txt", "r") as f:
        expected = f.read().strip("\n")
    assert f"{data}" == expected


def test_parser_json():
    before = "tests/fixtures/before.json"
    after = "tests/fixtures/after.json"
    data = parser(before, after)
    with open("tests/fixtures/before_after_dict.txt", "r") as f:
        expected = f.read().strip("\n")
    assert f"{data}" == expected


def test_parser_yml():
    before = "tests/fixtures/before.yaml"
    after = "tests/fixtures/after.yml"
    data = parser(before, after)
    with open("tests/fixtures/before_after_dict.txt", "r") as f:
        expected = f.read().strip("\n")
    assert f"{data}" == expected
