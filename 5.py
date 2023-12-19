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

day = 5
year = 2023

inp = get_input(day, year)

inp1 = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

inp = inp.strip().split('\n')

seeds = []

class Map:
    def __init__(self):
        self.ranges = []

    def add_range(self, range):
        self.ranges = sorted (self.ranges + [range], key = lambda x: x[1])

    def __call__(self, value):
        ret = value
        for range in self.ranges:
            if value < range[1]:
                ret = value
                break
            elif value < range[1] + range[-1]:
                ret = range[0] + value - range[1]
                break
        return ret

    def get_range(self, ranges):
        ret = []
        for inp in ranges:
            start = inp[0]
            end = inp[1]
            for range in self.ranges: 
                if end < range[1]:
                    ret.append([start, end])
                    start = end + 1
                    break
                if start < range[1]:
                    ret.append([start, range[1]-1])
                    start = range[1]
                if end < range[1] + range[-1]:
                    ret.append([range[0] + start - range[1], range[0] + end - range[1]])
                    start = end + 1
                    break
                elif start < range[1] + range[-1]:
                    ret.append([range[0] + start - range[1], range[0] + range[-1] -1 ])
                    start = range[1] + range[-1]
            if start < end:
                ret.append([start, end])
        ret = sorted(ret, key=lambda x: x[0])
        return ret

seed2soil = Map()
soil2fert = Map()
fert2water = Map()
water2light = Map()
light2temp = Map()
temp2hum = Map()
hum2loc = Map()

curr =  None

for l in inp:
    l = l.strip()
    if not l: continue
    if l.startswith('seeds:'):
        seeds = list(map(int, l.split(":")[1].split()))
    else:
        if l == 'seed-to-soil map:':
            curr = seed2soil
        elif l == 'soil-to-fertilizer map:':
            curr = soil2fert
        elif l == 'fertilizer-to-water map:':
            curr = fert2water
        elif l == 'water-to-light map:':
            curr = water2light
        elif l == 'light-to-temperature map:':
            curr = light2temp
        elif l == 'temperature-to-humidity map:':
            curr = temp2hum
        elif l == 'humidity-to-location map:':
            curr = hum2loc
        else:
            curr.add_range(list(map(int, l.split())))

def part1():
    min = 1e20
    for s in seeds:
        dist = hum2loc(temp2hum(light2temp(water2light(fert2water(soil2fert(seed2soil(s)))))))
        if dist < min:
            min = dist

    return min

def part2():
    r0 = []
    for i in range(0,len(seeds),2):
        r0.append([seeds[i], seeds[i]+seeds[i+1]-1])

    r0 = sorted(r0, key=lambda x: x[0])
    r1 = seed2soil.get_range(r0)
    r2 = soil2fert.get_range(r1)
    r3 = fert2water.get_range(r2)
    r4 = water2light.get_range(r3)
    r5 = light2temp.get_range(r4)
    r6 = temp2hum.get_range(r5)
    r7 = hum2loc.get_range(r6)
    s = r7[0][0]
    l = hum2loc(temp2hum(light2temp(water2light(fert2water(soil2fert(seed2soil(s)))))))
    return s


result_1 = part1()
result_2 = part2()
print("Part 1:", result_1)
print("Part 2:", result_2)

#submit_result(day, year, 1, result_1)
#submit_result(day, year, 2, result_2)
