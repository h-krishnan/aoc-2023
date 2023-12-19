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

day = 9
year = 2023

inp = get_input(day, year)

inp1 = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45

"""

inp = inp.strip().split('\n')

def part1():
    s = 0
    for l in inp:
        series = [l:= [int(x) for x in l.strip().split()] ]
        while True:
            series.append(l := [l[i+1] - l[i] for i in range(len(l)-1)])
            if all(x == 0 for x in l): break
        s += sum(x[-1] for x in series)
    return s

def part2():
    s = 0
    for l in inp:
        series = [l:= [int(x) for x in l.strip().split()] ]
        while True:
            series.append(l := [l[i+1] - l[i] for i in range(len(l)-1)])
            if all(x == 0 for x in l): break
        s += sum((-1)**i*x[0] for i, x in enumerate(series))
    return s

result_1 = part1()
result_2 = part2()
print("Part 1:", result_1)
print("Part 2:", result_2)

#submit_result(day, year, 1, result_1)
#submit_result(day, year, 2, result_2)
