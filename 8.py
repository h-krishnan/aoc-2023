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

day = 8
year = 2023

inp = get_input(day, year)

inp = inp.strip().split('\n')

inst = inp[0]

nodes = {}

for l in inp[2:]:
    t = l.split('=')
    n = t[0].strip()
    t = [x.strip() for x in t[1].strip()[1:-1].split(',')]
    nodes[n] = t

def solve(part, nodes):
    if part == 1:
        anodes = ['AAA']
        target_reached = lambda x: x == 'ZZZ'
    else:
        anodes = [x for x in nodes if x[-1] == 'A']
        target_reached = lambda x: x[-1] == 'Z'
    path = []
    orig = anodes[:]
    count = 0
    moves = [itertools.cycle(inst) for x in anodes] 
    
    self = {}
    reach_z = {}
    
    done = False
    for i, (curr, moveiter) in enumerate(zip(anodes, moves)):
        count = 0
        while True:
            count += 1
            move = next(moveiter)
            if move == 'L':
                curr = nodes[curr][0]
            else:
                curr = nodes[curr][1]
    
            if curr == orig[i]:
                if i not in self:
                    self[i] = count

            
            path.append(curr)
            if target_reached(curr):
                path = []
                break
        reach_z[i] = count
    
    return (math.lcm(*reach_z.values()))

result_1 = solve(1, nodes)
result_2 = solve(2, nodes)
print("Part 1:", result_1)
print("Part 2:", result_2)

#submit_result(day, year, 1, result_1)
#submit_result(day, year, 2, result_2)
