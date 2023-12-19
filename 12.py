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

day = 12
year = 2023

inp = get_input(day, year)

inp = [l.strip().split() for l in inp.strip().split('\n') ]

lines = inp


@functools.cache
def calculate1(slots, start_slots, pattern, start_pattern):
    if start_slots == len(slots):
        if start_pattern == len(pattern):
            return 1
        else:
            return 0
    dots, hashes = slots[start_slots]
    s = 0
    for x in dots:
        if '#' in pattern[start_pattern:start_pattern + x]:
            continue
        if start_pattern + x + hashes > len(pattern):
            continue
        if '.' in pattern[start_pattern + x:start_pattern + x + hashes]:
            continue
        s += calculate1(slots, start_slots + 1, pattern, start_pattern + x + hashes)
    return s

    


def calculate(pattern, count):
    # total no. of dots
    ndots = len(pattern) - sum(count)
    # no. of dots at a gap -- every gap requires a gap
    ndots -= len(count)-2
    nslots = [tuple(range(1, ndots+1))]*len(count)
    nslots[0] = tuple([0]) + nslots[0]

    nslots = tuple(zip(nslots, count))
    nslots = nslots + tuple([tuple([tuple(range(ndots+1)), 0])])
    
    return calculate1(nslots, 0, pattern, 0)


def solve(part):
    factor = 1 if part == 1 else 5
    s = 0
    for p,c in lines:
        c1 = tuple(int(x) for x in c.split(','))
        p = "?".join([p]*factor)
        c1 = c1*factor
        v = calculate(p, c1)
        s += v
    return s

result_1 = solve(1)
result_2 = solve(2)
print("Part 1:", result_1)
print("Part 2:", result_2)

#submit_result(day, year, 1, result_1)
#submit_result(day, year, 2, result_2)
