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

day = 4
year = 2023

inp = get_input(day, year)

inp = [l.strip().split(":")[1].split("|") for l in inp.strip().split('\n')]
inp = [ (set(y.split()), set(z.split())) for (y,z) in inp]

def part_1():
    return sum( 2**(x-1) for w,n in inp if (x := len(w & n)) > 0)

def part_2():
   wins = [1]*len(inp)
   for c, (winners, numbers) in enumerate(inp):
      for x in range(nwins := len(numbers & winners)):
          if c + x + 1 < len(wins):
              wins[c+x+1] += wins[c]
   return sum(wins)


result_1 = part_1()
result_2 = part_2()
print("Part 1:", result_1)
print("Part 2:", result_2)

#submit_result(day, year, 1, result_1)
#submit_result(day, year, 2, result_2)
