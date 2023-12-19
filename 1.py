import sys
from collections import defaultdict
from itertools import permutations, combinations
import functools
import itertools
import math
import re
import heapq
import time
from aoctools import dijkstra
from aoctools import get_input, submit_result
from math import *

day = 1
year = 2023

inp = get_input(day, year)

inp1 = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

inp1 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

inp = inp.strip()
inp = inp.split('\n')
inp = [l.strip() for l in inp]

num = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def solve(part):
    s = 0
    for i in inp:
        start = None
        end = None
        for item in re.finditer("(?=\\d" + ("" if part == 1 else "|" + "|".join(num)) + ")", i):
            if start is None: start = item.span()[0]
            end = item.span()[0]
        if i[start].isdigit():
            start = int(i[start])
        else:
            start = num.index([j for j in num if i[start:].startswith(j)][0]) + 1
        if i[end].isdigit():
            end = int(i[end])
        else:
            end = num.index([j for j in num if i[end:].startswith(j)][0]) + 1
        s += start*10 + end
    return s

result_1 = solve(1)
result_2 = solve(2)
print("Part 1:", result_1)
print("Part 2:", result_2)

#submit_result(day, year, 1, result_1)
#submit_result(day, year, 2, result_2)
