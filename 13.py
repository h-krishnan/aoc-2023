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

day = 13
year = 2023

inp = get_input(day, year)

inp1 = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""


inp = inp.strip().split('\n')

patterns = []

pattern = []
for l in inp:
    l = l.strip()
    if l == "":
        if pattern:
            patterns.append(pattern)
        pattern = []
    else:
        pattern.append(l)

patterns.append(pattern)

def get_score(pattern, old):
    # horizontal
    h = None
    l = len(pattern)
    for x in range(1, l):
        found = True
        for w in range(min(x,l-x+1)):
            if x-w-1 < 0:
                break
            if x+w >= l:
                break
            if pattern[x-w-1] != pattern[x+w]:
                found = False
                break
        if found:
            h = 100*x
            if h != old:
                return h
    # vertical
    nc = len(pattern[0])
    L = list(itertools.chain(*pattern))
    pattern = [L[i::nc] for i in range(nc)]
    pattern = ["".join(x) for x in pattern]
    h = None
    l = len(pattern)
    for x in range(1, l):
        found = True
        for w in range(min(x, l-x+1)):
            if x-w-1 < 0:
                break
            if x+w >= l:
                break
            if pattern[x-w-1] != pattern[x+w]:
                found = False
                break
        if found:
            h = x
            if h != old:
                return h
    return None

def part_1():
    s = 0
    for pattern in patterns:
        s += get_score(pattern, None)
    return s

def part_2():
    s = 0
    for pattern in patterns:
        oc = get_score(pattern, None)
        pcopy = [[x for x in p] for p in pattern]
        done = False
        m = set()
        for i, l in enumerate(pattern):
            for j, v in enumerate(l):
                orig = pcopy[i][j]
                if orig == '#':
                    pcopy[i][j] = '.'
                else:
                    pcopy[i][j] = '#'
                pat = ["".join(x) for x in pcopy]
                v = get_score(pat, oc)
                pcopy[i][j] = orig
                if v and v != oc:
                    m.add(v)
                    done = True
                    break
            if done:
                break
        s += m.pop()
    return s

result_1 = part_1()
result_2 = part_2()
print("Part 1:", result_1)
print("Part 2:", result_2)

#submit_result(day, year, 1, result_1)
#submit_result(day, year, 2, result_2)
