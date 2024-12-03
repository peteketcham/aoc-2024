#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# example
# a = [3, 4, 2, 1, 3, 3]
# b = [4, 3, 5, 3, 9, 3]

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
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    vector = []
    for i, x in enumerate(sorted_a):
        # print(abs(x - sorted_b[i]), end=' ')
        vector.append(abs(x - sorted_b[i]))
    print(sum(vector))

if __name__ == "__main__":
    main()