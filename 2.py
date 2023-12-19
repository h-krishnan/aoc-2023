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

day = 2
year = 2023

inp = get_input(day, year)

inp = inp.strip().split('\n')

def part_1(inp):
    possible = dict(
            red = 12,
            green = 13,
            blue = 14
            )

    s = 0
    for g, l in enumerate(inp):
        l = l.strip().split(':')[1].split(";")
        found = True
        for set in l:
            set = set.split()
            set.reverse()
            items = iter(set)
            while True:
                try:
                    name = next(items)
                    name = name.strip()
                    name = name.replace(",","")
                    value = int(next(items))
                    if value > possible[name]:
                        found = False
                        break
                except StopIteration:
                    break
            if not found:
                break
        if found:
            s += g+1

    return s

def part_2(inp):
    s = 0
    for g, l in enumerate(inp):
        l = l.strip().split(':')[1].replace(",", "").split(";")
        mr = -1e20
        mb = -1e20
        mg = -1e20
        for set in l:
            set = set.split()
            set.reverse()
            items = iter(set)
            while True:
                try:
                    name = next(items)
                    name = name.strip()
                    value = int(next(items))
                    if name == "red":
                        if value > mr:
                            mr = value
                    elif name == "blue":
                        if value > mb:
                            mb = value
                    elif name == "green":
                        if value > mg:
                            mg = value
                except StopIteration:
                    break
        s += max(mr,1)*max(mb,1)*max(mg,1)
    return s

result_1 = part_1(inp)
result_2 = part_2(inp)
print("Part 1:", result_1)
print("Part 2:", result_2)

#submit_result(day, year, 1, result_1)
#submit_result(day, year, 2, result_2)
