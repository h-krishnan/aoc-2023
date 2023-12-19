from collections import defaultdict
from itertools import permutations, combinations
import functools
import itertools
import math
import re
import heapq
import time
from aoctools import get_input, submit_result
from aoctools import dijkstra
from math import *

result = None

day = 18
year = 2023

inp = get_input(day, year)

import time
t = time.time()

inp1 = r"""
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""

inp1 = r"""
R 3 abc
D 2 abc
L 1 abc
D 1 abc
L 2 abc
U 3 abc
"""

inp = inp.strip().split('\n')

dmap = {'R' : (0,1), 'L' : (0,-1), 'U' : (-1,0), 'D' : (1,0) }
cmap = { '0' : 'R', '1' : 'D', '2' : 'L', '3' : 'U' }

def solve(inp, part):
    curr = (0,0)
    p = (0,0)
    s = 0
    for l in inp:
        d, c, color = l.strip().split()
        if part == 2:
            d = cmap[color[-2]]
            c = int('0x' + color[2:-2], 16)
        else:
            c = int(c)

        d = dmap[d]
        curr = curr[0] + d[0]*c, curr[1] + d[1]*c
   
        s += (p[1]*curr[0] - p[0]*curr[1])
        s += (abs(curr[0] - p[0]) + abs(curr[1] - p[1]))
        p = curr
    return int(s/2) + 1

result_1 = solve(inp, 1)
result_2 = solve(inp, 2)
print ("Part 1:", result_1)
print ("Part 2:", result_2)
print (f"Time taken: {time.time() -t }s")


#submit_result(day, year, 1, result_1)
#submit_result(day, year, 2, result_2)
