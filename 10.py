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

day = 10
year = 2023

inp = get_input(day, year)

inp1 = """
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""

inp1 = """
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""


inp = inp.strip().split('\n')

pipes = {}
s = None


for r, l in enumerate(inp):
    for c, p in enumerate(l.strip()):
        if p == '|':
            pipes[(r,c)] = [(r-1,c),(r+1,c)], '|'
        elif p == '-':
            pipes[(r,c)] = [(r,c-1),(r,c+1)], '-'
        elif p == 'L':
            pipes[(r,c)] = [(r-1,c),(r,c+1)], 'L'
        elif p == 'J':
            pipes[(r,c)] = [(r-1,c), (r,c-1)], 'J'
        elif p == '7':
            pipes[(r,c)] = [(r+1,c), (r,c-1)], '7'
        elif p == 'F':
            pipes[(r,c)] = [(r,c+1), (r+1,c)], 'F'
        elif p == '.':
            pass
        elif p == 'S':
            s = (r,c)

nr = len(inp)
nc = len(inp[0].strip())

def part_1():
    for j1 in [(-1,0),(1,0),(0,-1),(0,1)]:
        n1 = pipes.get((s[0] + j1[0], s[1] + j1[1]))
        if not n1:
            continue
        if n1[0].count(s) == 0:
            continue
        for j2 in [(-1,0),(1,0),(0,-1),(0,1)]:
            if j1 == j2:
                continue
            n2 = pipes.get((s[0] + j2[0], s[1] + j2[1]))
            if not n2:
                continue
            if n2[0].count(s) == 0:
                continue

            pipes[s] = [ (s[0] + j1[0], s[1] + j1[1]), (s[0] + j2[0], s[1] + j2[1]) ], None

            c = 0
            prev = pipes[s][0][0]
            curr = s
            path = [s]
            valid = True
            while True:
                (d1, d2),w = pipes.get(curr)
                if d1 == prev:
                    prev = curr
                    curr = d2
                elif d2 == prev:
                    prev = curr
                    curr = d1
                else:
                    print ("both d1 and d2 not found", n1, n2)
                    valid = False
                    break
                c += 1
                if curr == s:
                    valid = True
                    return path, c//2
                    break
                else:
                    path.append(curr)
                if c > len(pipes):
                    print ("out of range", n1, n2)
                    valid = False
                    break
            if valid:
               break
        if valid:
            break


inside = set()

def part2():
    ps = pipes[s][0]
    n1 = ps[0]
    n2 = ps[1]
    m1 = pipes[n1][1]
    m2 = pipes[n2][1]

    if m1 in ('-', '7', 'J', 'F',  'L'):
        if m2 in ('-', '7', 'J', 'F', 'L'):
            w = '-'
        elif m2[1] == '|':
            if n1[0] < n2[0] and n1[1] < n2[1]:
                w = '7'
            elif n2[0] < n1[0] and n2[1] < n1[1]:
                w = '7'
            elif n1[0] > n2[0] and n1[1] < n2[1]:
                w = 'J'
            elif n2[0] > n1[0] and n2[1] < n1[1]:
                w = 'J'
            if n1[0] < n2[0] and n1[1] > n2[1]:
                w = 'F'
            elif n2[0] < n1[0] and n2[1] > n1[1]:
                w = 'F'
            if n1[0] > n2[0] and n1[1] > n2[1]:
                w = 'L'
            elif n2[0] > n1[0] and n2[1] > n1[1]:
                w = 'L'
    elif m2 in ('-', '7', 'J', 'F', 'L'):
        if m1 in ('-', '7', 'J', 'F', 'L'):
            w = '-'
        elif m1 == '|':
            if n1[0] < n2[0] and n1[1] < n2[1]:
                w = '7'
            elif n2[0] < n1[0] and n2[1] < n1[1]:
                w = '7'
            elif n1[0] > n2[0] and n1[1] < n2[1]:
                w = 'J'
            elif n2[0] > n1[0] and n2[1] < n1[1]:
                w = 'J'
            if n1[0] < n2[0] and n1[1] > n2[1]:
                w = 'F'
            elif n2[0] < n1[0] and n2[1] > n1[1]:
                w = 'F'
            if n1[0] > n2[0] and n1[1] > n2[1]:
                w = 'L'
            elif n2[0] > n1[0] and n2[1] > n1[1]:
                w = 'L'
         
    if w is None:
        valid = False
        print ("invalid configuration", n1, n2, m1, m2)
        exit(1)

    pipes[s] = pipes[s][0], w

    sum = 0
    for r in range(nr):
        nint = 0
        inF = False
        inL = False
        for c in range(nc):
            if (r,c) in path:
                w = pipes.get((r,c))
                if w[1] == 'F':
                    inF = True
                elif w[1] == 'L':
                    inL = True
                elif w[1] == '7':
                    if inF:
                        inF = False
                    elif inL:
                        nint += 1
                        inL = False
                    else:
                        print( "got 7 but not in F or L", r, c)
                        break
                elif w[1] == 'J':
                    if inF:
                        nint += 1
                        inF = False
                    elif inL:
                        inL = False
                        pass
                    else:
                        print( "got 7 but not in F or L", r, c)
                        break
                elif w[1] == '-':
                    if not inL and not inF:
                        print( "got - but not in F or L", r, c)
                        break
                elif w[1] == '|':
                    nint += 1
                else:
                    print ("Unknown w", w)
            elif nint % 2 == 1:
                inside.add((r,c))
                sum += 1
    return sum


def print_path():
    for r in range(nr):
        for c in range(nc):
            if (r,c) in path:
                w = pipes[(r,c)]
                m = { '-': '2500', '|' : '2502', 'L' : '2514', 'J' : '2518', '7' : '2510', 'F' : '250C' }
                print ( eval("u'\\u" + m[w[1]] + "'"), end='')
            elif (r,c) in inside:
                print ( eval("u'\\u" + '2588' + "'"), end='')
            else:
                print(' ',end='')
        print()
    print()

path, part1 = part_1()
result_1 = part1
result_2 = part2()
print("Part 1:", result_1)
print("Part 2:", result_2)

print_path()

#submit_result(day, year, 1, result_1)
#submit_result(day, year, 2, result_2)
