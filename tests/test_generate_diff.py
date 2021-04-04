#!/usr/bin/env python3

from gendiff.gendiff import generate_diff


def test_generate_diff():
    before = "tests/fixtures/before.json"
    after = "tests/fixtures/after.json"
    data = generate_diff(before, after)
    json_diff = open("tests/fixtures/json_diff.txt", "r")
    expected = json_diff.read().strip("\n")
    json_diff.close()
    assert data == expected
