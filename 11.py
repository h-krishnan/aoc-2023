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

day = 11
year = 2023

inp = get_input(day, year)

inp1 = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""


inp = inp.strip().split('\n')


def solve(inp, part):
    gs = set()
    for r, l in enumerate(inp):
        for c, x in enumerate(l.strip()):
            if x == '#':
                gs.add((r,c))

    nr = len(inp)
    nc = len(inp[0].strip())

    empty_rows = []
    empty_cols = []
    
    for r in range(nr):
        empty = True
        for c in range(nc):
            if (r,c) in gs:
                empty = False
                break
        if empty:
            empty_rows.append(r)
    
        empty = True
        for c in range(nc):
            if (c,r) in gs:
                empty = False
                break
        if empty:
            empty_cols.append(r)
    
    if part == 1:
        increase_by = 1
    else:
        increase_by = 1000000-1

    for r in empty_rows[::-1]:
        for g in list(x for x in gs):
            if g[0] > r:
                gs.remove(g)
                gs.add((g[0]+increase_by, g[1]))
    
    for c in empty_cols[::-1]:
        for g in list(x for x in gs):
            if g[1] > c:
                gs.remove(g)
                gs.add((g[0], g[1]+increase_by))
    
    
    s = 0
    for x,y in itertools.product(gs, gs):
        if x == y:
            continue
        s += abs(x[0] - y[0]) + abs(x[1] - y[1])
    
    return s//2

result_1 = solve(inp, 1)
result_2 = solve(inp, 2)
print("Part 1:", result_1)
print("Part 2:", result_2)

#submit_result(day, year, 1, result_1)
#submit_result(day, year, 2, result_2)
