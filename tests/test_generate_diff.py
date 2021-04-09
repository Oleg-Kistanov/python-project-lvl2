#!/usr/bin/env python3

from gendiff.gendiff import generate_diff


def test_generate_diff_json():
    before = "tests/fixtures/before.json"
    after = "tests/fixtures/after.json"
    data = generate_diff(before, after)
    with open("tests/fixtures/json_diff.txt", "r") as json_diff:
        expected = json_diff.read().strip("\n")
    assert data == expected


def test_generate_diff_yml():
    before = "tests/fixtures/before.yaml"
    after = "tests/fixtures/after.yml"
    data = generate_diff(before, after)
    with open("tests/fixtures/yml_diff.txt", "r") as yml_diff:
        expected = yml_diff.read().strip("\n")
    assert data == expected
