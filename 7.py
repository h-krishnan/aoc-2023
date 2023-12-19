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

day = 7
year = 2023

inp = get_input(day, year)

inp1 = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

s = 0
inp = inp.strip().split('\n')

def get_order(part):
    if part == 1:
        return "AKQJT98765432"
    else:
        return "AKQT98765432J"

nonj = 'AKQT98765432'

@functools.lru_cache(maxsize=None)
def rank(card, part):
    if part == 2 and 'J' in card:
        minr = 10
        for l in nonj:
            r = rank(card.replace('J', l, 1), part)
            if r < minr:
                minr = r
        return minr

    d = defaultdict(int)
    for c in card:
        d[c] += 1
    if len(d) == 1:
        return 1
    if len(d) == 2:
        if 4 in d.values():
            return 2
        else:
            return 3
    if len(d) == 3:
        if 3 in d.values():
            return 4
        else:
            return 5
    if len(d) == 4:
        return 6
    else:
        return 7


def compare(card1, card2, part):
    card1 = card1[0]
    card2 = card2[0]
    r1 = rank(card1, part)
    r2 = rank(card2, part)
    if r1 == r2:
        order = get_order(part)
        for c1, c2 in zip(card1, card2):
            if order.index(c1) < order.index(c2):
                return -1
            elif order.index(c1) > order.index(c2):
                return 1
    elif r1 < r2:
        return -1
    else:
        return 1

def get_value(cards, part):
    cmp = lambda x, y: compare(x,y,part)
    cards  = sorted(cards, key = functools.cmp_to_key(cmp), reverse=True)
    s = 0
    for i, c in enumerate(cards):
        s += (1+i)*int(c[1])
    return s

def part1(cards):
    return get_value(cards, 1)

def part2(cards):
    return get_value(cards, 2)

cards = []
for l in inp:
    cards.append(l.strip().split())

result_1 = part1(cards)
result_2 = part2(cards)
print("Part 1:", result_1)
print("Part 2:", result_2)

#submit_result(day, year, 1, result_1)
#submit_result(day, year, 2, result_2)
