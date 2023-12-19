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

day = 6
year = 2023

inp = get_input(day, year)

inp = inp.strip().split('\n')

def fun(inp, part):
    time = inp[0].split(":")[1].strip()
    if part == 2:
        time = "".join(time.split())
    dist = inp[1].split(":")[1].strip()
    if part == 2:
        dist = "".join(dist.split())


    time = list(map(int, time.split()))
    dist = list(map(int, dist.split()))

    p = 1
    for t, d in zip(time, dist):
        s = 0
        for n in range(t):
            if (t-n)*n >= d:
                s += 1
            elif s > 0:
                break

        p *= s #um(1 for n in range(t) if (t-n)*n >= d)
    return p

result_1 = fun(inp, 1)
result_2 = fun(inp, 2)
print("Part 1:", result_1)
print("Part 2:", result_2)

#submit_result(day, year, 1, result_1)
#submit_result(day, year, 2, result_2)
