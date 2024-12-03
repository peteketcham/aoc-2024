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


def _is_safe(level):
    if level == sorted(level) or level == sorted(level, reverse=True):
        for i in range(len(level) - 1):
            if 0 < abs(level[i] - level[i + 1]) <= 3:
                pass
            else:
                return False
        return True
    return False


def main():
    levels = parse_input()
    safe = 0
    for level in levels:
        if _is_safe(level):
            safe += 1
        else:
            for i in range(len(level)):
                temp = level[:]
                temp.pop(i)
                if _is_safe(temp):
                    safe += 1
                    break
    print(safe)


if __name__ == "__main__":
    main()