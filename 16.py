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

day = 16
year = 2023

inp = get_input(day, year)

inp1 = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""

inp = inp.strip().split('\n')

ms = {}

for r, l in enumerate(inp):
    for c, m in enumerate(l.strip()):
        if m == '.':
            pass
        else:
            ms[(r,c)] = m

nrows = len(inp)
ncols = len(inp[0])

def print_board(cells, bs):
    for r in range(nrows):
        for c in range(ncols):
            found = False
            for b, curr in bs:
                if curr == (r,c):
                    if curr[1] > b[1]:
                        print (">", end="")
                    elif curr[1] < b[1]:
                        print ("<", end="")
                    elif curr[0] > b[0]:
                        print ("v", end="")
                    elif curr[0] < b[0]:
                        print ("^", end="")
                    else:
                        print("*", end="")
                    found = True
                    break
            if not found:
                if (r,c) in cells:
                    print ('#', end = "")
                elif (r,c) in ms:
                    print (ms[(r,c)], end="")
                else:
                    print(".", end="")
        print()
    print()


def fn(bs):
    processed = set()
    cells = set()
    while bs:
        #print_board([], [])
        #print_board(cells, bs)
        b = bs.pop(0)
        if b in processed:
            continue
        processed.add(b)
        m = ms.get(b[1])
        cells.add(b[1])
        toadd = []
        if m == '|':
            if b[0][1] == b[1][1]:
                nr = 2*b[1][0] - b[0][0]
                nc = b[1][1]
                toadd.append(((b[1], (nr,nc))))
            else:
                nr = b[1][0]-1
                nc = b[1][1]
                toadd.append(((b[1], (nr,nc))))
                nr = b[1][0]+1
                nc = b[1][1]
                toadd.append(((b[1], (nr,nc))))
        elif m == '-':
            if b[0][0] == b[1][0]:
                nc = 2*b[1][1] - b[0][1]
                nr = b[1][0]
                toadd.append(((b[1], (nr,nc))))
            else:
                nc = b[1][1]-1
                nr = b[1][0]
                toadd.append(((b[1], (nr,nc))))
                nc = b[1][1]+1
                nr = b[1][0]
                toadd.append(((b[1], (nr,nc))))
        elif m == '\\':
            if b[0][0] == b[1][0]:
                if b[1][1] > b[0][1]:
                    nc = b[1][1]
                    nr = b[1][0] + 1
                    toadd.append(((b[1], (nr,nc))))
                else:
                    nc = b[1][1]
                    nr = b[1][0] - 1
                    toadd.append(((b[1], (nr,nc))))
            else:
                if b[1][0] > b[0][0]:
                    nc = b[1][1] + 1
                    nr = b[1][0]
                    toadd.append(((b[1], (nr,nc))))
                else:
                    nc = b[1][1] - 1
                    nr = b[1][0]
                    toadd.append(((b[1], (nr,nc))))
        elif m == '/':
            if b[0][0] == b[1][0]:
                if b[1][1] > b[0][1]:
                    nc = b[1][1]
                    nr = b[1][0] - 1
                    toadd.append(((b[1], (nr,nc))))
                else:
                    nc = b[1][1]
                    nr = b[1][0] + 1
                    toadd.append(((b[1], (nr,nc))))
            else:
                if b[1][0] > b[0][0]:
                    nc = b[1][1] - 1
                    nr = b[1][0]
                    toadd.append(((b[1], (nr,nc))))
                else:
                    nc = b[1][1] + 1
                    nr = b[1][0]
                    toadd.append(((b[1], (nr,nc))))
        else:
            if b[0][0] == b[1][0]:
                nc = 2*b[1][1] - b[0][1]
                nr = b[1][0]
                toadd.append(((b[1], (nr,nc))))
            else:
                nr = 2*b[1][0] - b[0][0]
                nc = b[1][1]
                toadd.append(((b[1], (nr,nc))))
        for from_,to in toadd:
            if to[0] < 0 or to[1] < 0:
                continue
            if to[0] >= nrows:
                continue
            if to[1] >= ncols:
                continue
            bs.append((from_, to))

    return len(cells)

def part_1():
    return fn([((0,-1),(0,0))])

def part_2():
    m = -1e20
    for r in range(nrows):
        b = [((r,-1),(r,0))]
        v = fn(b)
        if v > m:
            m = v
        b = [((r,ncols),(r,ncols-1))]
        v = fn(b)
        if v > m:
            m = v

    for c in range(ncols):
        b = [((-1,c),(0,c))]
        v = fn(b)
        if v > m:
            m = v
        b = [((nrows,c),(nrows-1,c))]
        v = fn(b)
        if v > m:
            m = v
    return m

    
result_1 = part_1()
result_2 = part_2()
print ("Part 1: ", result_1)
print ("Part 2: ", result_2)

#submit_result(day, year, 1, result_1)
#submit_result(day, year, 2, result_2)
