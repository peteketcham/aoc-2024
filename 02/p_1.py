#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def parse_input():
    formatted_result = []
    with open("input.txt", "r") as input:
        for line in input:
            line = line.strip('\n')
            line = line.split()
            formatted_result.append([int(x) for x in line])
    return formatted_result


def main():
    levels = parse_input()
    safe = 0
    for level in levels:
        if level == sorted(level) or level == sorted(level, reverse=True):
            safety_flag = True
            for i in range(len(level) - 1):
                if safety_flag and 0 < abs(level[i] - level[i + 1]) <= 3:
                    pass
                else:
                    safety_flag = False
            if safety_flag:
                safe += 1

    print(safe)


if __name__ == "__main__":
    main()