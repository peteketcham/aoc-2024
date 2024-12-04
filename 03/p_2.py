#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import mul
import re
from functools import reduce
from pprint import pprint

def parse_input():
    formatted_result = []
    with open("input.txt", "r") as input:
        for line in input:
            line = line.strip("\n")
            formatted_result.append(line)
    return "".join(formatted_result)


def main():
    """parse string to find the sum of instances of 'mul(x, y)"""
    """
            0
           / \
         do  /\
            /  \
           don't  do
        [do, [don't, do], [don't, do], ...]
    """
    _mul = r"mul\(\d+,\d+\)"
    _do = r"do\(\)"
    _dont = r"don't\(\)"
    line = parse_input()
    mul_sum = 0
    # positions of all the do() functions
    dos = [m.start(0) for m in re.finditer(_do, line)]
    # positions of all the don't() functions
    donts = [m.start(0) for m in re.finditer(_dont, line)]
    # positions of all the mul() functions and their values
    muls = [(m.start(0), m.group()) for m in re.finditer(_mul, line)]

    poi = sorted(dos + donts + [x[0] for x in muls])
    flag = True
    for point in poi:
        if point in dos:
            flag = True
        elif point in donts:
            flag = False
        else:
            if flag:
                a = [value for value in muls if value[0] == point][0]
                b = eval(a[1][3:])
                # here = reduce(lambda x, y: x * y, b)
                here = b[0] * b[1]
                mul_sum += here
    # ###
    # # valid mul() functions are those
    # # - before the first don't() function
    # # - after a do() function and before the next don't() function
    # # - after a do() function and to the end of the string

    # # sum of all the mul() functions before the first don't()
    # first = [eval(x[1][3:]) for x in muls if x[0] < donts[0]]
    # mul_sum += sum(reduce(lambda a, y: a * y, x) for x in first)

    # do_muls = []

    # # drop all the mul() and do() before the first don't()
    # muls = [x for x in muls if x[0] > donts[0]]
    # dos = [x for x in dos if x > donts[0]]

    # # 2
    # while dos:
    #     do = dos.pop(0)
    #     # drop all the don't()s and mul()s before the do
    #     donts = [x for x in donts if x > do]
    #     muls = [x for x in muls if x[0] > do]
    #     # 3
    #     if not donts:
    #         do_muls += [eval(x[1][3:]) for x in muls]
    #         break
    #     # grab and drop all the muls between the do and the next don't
    #     do_muls += [eval(x[1][3:]) for x in muls if x[0] < donts[0]]
    #     muls = [x for x in muls if x[0] > donts[0]]

    #     # drop any/all the dos before the next don't  -- this should do nothing
    #     dos = [x for x in dos if x > donts[0]]
    # # print(first, do_muls)
    # # print(sum(reduce(lambda a, y: a * y, x) for x in first),
    # #       sum(reduce(lambda a, y: a * y, x) for x in do_muls))
    # mul_sum += sum(reduce(lambda a, y: a * y, x) for x in do_muls)

    # # match = re.split(r"don't\(\)", line)
    # # match = [re.split(r"do\(\)", x) for x in match]
    # # m_2 = []
    # # for x in match:
    # #     m_2.append([re.findall(_mul, y) for y in x])
    # # do_first = [reduce(lambda a, y: a * y, eval(x[3:])) for x in m_2[0][0]]
    # # do_rest = []
    # # for donts in m_2[1:]:
    # #     if len(donts) > 1:
    # #         do_rest.append([reduce(lambda a, y: a * y, eval(x[3:])) for x in [item for sublist in donts[1:] for item in sublist]])
    # # print(sum(do_first) + sum(sum(x) for x in do_rest))
    # # mul_sum += sum(do_first) + sum(sum(x) for x in do_rest)
    print(mul_sum)


if __name__ == "__main__":
    main()
