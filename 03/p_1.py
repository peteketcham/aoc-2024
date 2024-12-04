#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from functools import reduce


def parse_input():
    formatted_result = []
    with open("input.txt", "r") as input:
        for line in input:
            line = line.strip("\n")
            formatted_result.append(line)
    return formatted_result


def main():
    """parse string to find the sum of instances of 'mul(x, y)"""
    match_pattern = r"mul\(\d+,\d+\)"
    input_data = parse_input()
    mul_sum = 0
    for line in input_data:
        match = re.findall(match_pattern, line)
        match = [reduce(lambda a, y: a * y, eval(x[3:])) for x in match]
        mul_sum += sum(match)
    print(mul_sum)


if __name__ == "__main__":
    main()
