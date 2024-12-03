#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter

def parse_input():
    formatted_result = []
    with open("input.txt", "r") as input:
        a, b = [], []
        for line in input:
            line = line.strip('\n')
            line = line.split()
            a.append(int(line[0]))
            b.append(int(line[1]))
        formatted_result = [a, b]
    return formatted_result


def main():
    a, b = parse_input()
    sorted_a = Counter(a)
    sorted_b = Counter(b)
    vector = 0
    for i in sorted_a:
        vector += i * sorted_b[i]
    print(vector)

if __name__ == "__main__":
    main()