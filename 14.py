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

day = 14
year = 2023

inp = get_input(day, year)

inp1 = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

debug = False

inp = inp.strip().split('\n')

balls = set()
rocks = set()

toplayer = set()

for r, l in enumerate(inp):
    for c, b in enumerate(l.strip()):
        if b == 'O':
            balls.add((r,c))
        elif b == '#':
            rocks.add((r,c))

nr = len(inp)
nc = len(inp[0].strip())

def rotate(balls, rocks):
    if debug:
        print ("before rotation:")
        print_board(balls, rocks)
    nb = set()
    nw = set()
    for r,c in balls:
        nb.add((c,(nr-r-1)))
    for r,c in rocks:
        nw.add((c,(nr-r-1)))
    if debug:
        print ("after rotation:")
        print_board(nb, nw)
    return nb, nw

def get_score(balls):
    s = 0
    for r,c in balls:
        s += nr-r
    return s

def process(balls, rocks):
    done = False
    while not done:
        done = True
        nb = set()
        for r in range(nr):
            for c in range(nc):
                if (r,c) in balls:
                    if (r-1,c) in nb:
                        nb.add((r,c))
                    elif (r-1,c) in rocks:
                        nb.add((r,c))
                    else:
                        if r == 0:
                            nb.add((r,c))
                        else:
                            nb.add((r-1,c))
                            done = False
        balls = nb
    return balls

def part_1(balls, rocks):
    balls = process(balls, rocks)
    return get_score(balls)

def cycle(balls, rocks):
    balls = process(balls, rocks)
    balls, rocks = rotate(balls, rocks)
    balls = process(balls, rocks)
    balls, rocks = rotate(balls, rocks)
    balls = process(balls, rocks)
    balls, rocks = rotate(balls, rocks)
    balls = process(balls, rocks)
    balls, rocks = rotate(balls, rocks)
    return balls, rocks

def part_2(balls, rocks):
    patterns = {}
    plist = [balls]
    count = 0
    while True:
        balls, rocks = cycle(balls, rocks)
        count += 1
        b = tuple(sorted(list(balls)))
        plist.append(b)
        if b in patterns:
            repeat = count
            break
        patterns[b] = count

        if debug:
            print ("Count = ", count)
            print_board(balls, rocks)
            print()
            if count == 4:
                break

    index = plist.index(b)
    return get_score(plist[index + (1000000000 - index) % (repeat - index)])

def print_board(balls, rocks):
    for r in range(nr):
        for c in range(nc):
            if (r,c) in balls:
                print('O', end='')
            elif (r,c) in rocks:
                print('#', end='')
            else:
                print('.', end='')
        print()


result_1 = part_1(balls, rocks)
result_2 = part_2(balls, rocks)
print("Part 1:", result_1)
print("Part 2:", result_2)

#submit_result(day, year, 1, result_1)
#submit_result(day, year, 2, result_2)
