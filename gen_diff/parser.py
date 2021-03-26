#!/usr/bin/env python3

import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Generate diff"
    )
    parser.add_argument("first_file", nargs="?")
    parser.add_argument("second_file", nargs="?")

    return parser


def parse_arguments():
    parser = create_parser()
    namespace = parser.parse_args()
    return namespace
