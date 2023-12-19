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

day = 15
year = 2023

inp = get_input(day, year)

inp1 = """
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""

inp = inp.strip().split('\n')[0].split(',')

def hashing(string):
    s = 0
    for c in string:
        v = ord(c)
        s += v
        s *= 17
        s = s % 256
    return s

def part_1():
    s = 0
    for item in inp:
        s += hashing(item)
    return s

boxes = defaultdict(list)
def part_2():
    for item in inp:
        if '=' in item:
            item, value = item.split('=')
            value = int(value)
            b = hashing(item)
            found = False
            for i in boxes[b]:
                if i[0] == item:
                    i[1] = value
                    found = True
                    break
            if not found:
                boxes[b].append([item, value])
        elif '-' in item:
            item = item.split('-')[0]
            b = hashing(item)
            for v in boxes[b]:
                if v[0] == item:
                    boxes[b].remove(v)
                    break
        else:
            print ("Error", item)

    s = 0
    for k, v in boxes.items():
        for j, item in enumerate(v):
            s += (k + 1) * (j + 1) * item[1]
    return s

            
result_1 = part_1()
result_2 = part_2()
print ("Part 1:", result_1)
print ("Part 2:", result_2)


#submit_result(day, year, 1, result_1)
#submit_result(day, year, 2, result_2)
