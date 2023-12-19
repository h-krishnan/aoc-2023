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

day = 17
year = 2023

inp = get_input(day, year)

inp1 = r"""
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

inp = inp.strip().split('\n')

hl = {}

for r, l in enumerate(inp):
    for c, h in enumerate(l.strip()):
        hl[(r,c)] = int(h)

nrows = len(inp)
ncols = len(inp[0].strip())

start = (0,0)

start = ( (0,0), None, None )
startWt = 0

part = 1

def add_nbr(nbrs, point, ndir, ncount):
    npt = point[0] + ndir[0], point[1] + ndir[1]
    if npt[0] < 0 or npt[1] < 0 or npt[0] >= nrows or npt[1] >= ncols:
        pass
    else:
        nbr = hl[npt], (npt, ndir, ncount)
        nbrs.append (nbr)

def nbrFn(p):
    point, dir, ndir = p
    nbrs = []
    if not dir:
        add_nbr(nbrs, point, (1,0), 1)
        add_nbr(nbrs, point, (0,1), 1)
    else:
        if ndir < (3 if part ==1 else 10):
            add_nbr(nbrs, point, dir, ndir+1)
        if part == 1 or ndir >= 4:
            if dir[0]:
                add_nbr(nbrs, point, (0, 1), 1)
                add_nbr(nbrs, point, (0, -1), 1)
            else:
                add_nbr(nbrs, point, (1, 0), 1)
                add_nbr(nbrs, point, (-1, 0), 1)

    return nbrs

def target(p):
    return p[0] == (nrows-1, ncols-1)


def part1():
    global part
    part = 1
    return dijkstra(start, startWt, target, nbrFn)[0]

def part2():
    global part
    part = 2
    return dijkstra(start, startWt, target, nbrFn)[0]

result_1 = part1()
result_2 = part2()
print("Part 1:", result_1)
print("Part 2:", result_2)

#submit_result(day, year, 1, result_1)
#submit_result(day, year, 2, result_2)
