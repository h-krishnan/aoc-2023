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

day = 3
year = 2023

inp = get_input(day, year)

inp1 = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

inp = inp.strip()
inp = inp.split('\n')
inp = [l.strip() for l in inp]

s = 0

numbers = []
symbols = {}

for r, l in enumerate(inp):
    n = ""
    ns = 0
    for i, c in enumerate(l):
        if c == '.':
            if n:
                numbers.append((int(n), (r, (ns, i-1))))
                n = ""
        elif c.isdigit():
            if n == "":
                ns = i
            n = n + c
        else:
            if n:
                numbers.append((int(n), (r, (ns, i-1))))
                n = ""
            symbols[(r, i)] = c
    if n:
        numbers.append((int(n), (r, (ns, i-1))))
        n = ""

def part_1():
    s = 0
    for n, (r, pos) in numbers:
       if (r-1, pos[0]-1) in symbols or (r-1, pos[0]) in symbols or (r-1, pos[0]+1) in symbols:
           s += n
       elif (r+1, pos[0]-1) in symbols or (r+1, pos[0]) in symbols or (r+1, pos[0]+1) in symbols:
           s += n
       elif (r-1, pos[1]-1) in symbols or (r-1, pos[1]) in symbols or (r-1, pos[1]+1) in symbols:
           s += n
       elif (r+1, pos[1]-1) in symbols or (r+1, pos[1]) in symbols or (r+1, pos[1]+1) in symbols:
           s += n
       elif (r,pos[0]-1) in symbols or (r, pos[1]+1) in symbols:
           s += n
    return s

def part_2():
    s = 0
    gears = defaultdict(list)
    for n, (r, pos) in numbers:
        glist = []
        for nb in [ (r-1, pos[0]-1), (r-1, pos[0]), (r-1, pos[0]+1),
                    (r+1, pos[0]-1), (r+1, pos[0]), (r+1, pos[0]+1),
                    (r-1, pos[1]-1), (r-1, pos[1]), (r-1, pos[1]+1),
                    (r+1, pos[1]-1), (r+1, pos[1]), (r+1, pos[1]+1),
                    (r, pos[0]-1), (r, pos[1]+1) ]:
            sym = symbols.get(nb)
            if sym == '*':
                if nb not in glist:
                    glist.append(nb)
        for g in glist:
            gears[g].append(n)
    for g, ns in gears.items():
        if len(ns) == 2:
            s += ns[0]*ns[1]

    return s

result_1 = part_1()
result_2 = part_2()
print("Part 1:", result_1)
print("Part 2:", result_2)

#submit_result(day, year, 1, result_1)
#submit_result(day, year, 2, result_2)
