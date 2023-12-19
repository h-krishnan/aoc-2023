import sys
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

day = 19
year = 2023

inp = get_input(19, 2023)

inp1 = r"""
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""

inp = inp.strip().split('\n')

parts = []

def parse_input(inp):
    functions = {}
    parts = []
    parsing_rules = True
    for l in inp:
        if l == "":
            parsing_rules = False
            continue
        if parsing_rules:
            name, l = l.split('{')
            l = l[:-1]
            count = 1
            while l:
                cond = l.split(',', 1)
                if len(cond) == 2:
                    cond, l = cond
                    cond, true_value = cond.split(':')
                    if '<' in cond:
                        f, v  = cond.split('<')
                        v = int(v)
                        reverse = False
                    elif '>' in cond:
                        f, v = cond.split('>')
                        v = int(v) + 1
                        reverse = True
                    if ',' in l:
                        if reverse:
                            functions[name] = (f, v, name + "1", true_value) 
                        else:
                            functions[name] = (f, v, true_value, name + "1")
                        name = name + "1"
                    else:
                        if reverse:
                            functions[name] = (f, v, l, true_value) 
                        else:
                            functions[name] = (f, v, true_value, l)
                        break
        else:
            part = eval('dict(' + l[1:-1] + ')')
            parts.append(part)
    return parts, functions
    
def process(fn, ranges):
    ret = []
    true_ranges = []
    false_ranges = []
    x, cond, true, false = functions[fn]
    for r in ranges:
       xmin, xmax = r[x]

       if xmax < cond:
           true_ranges.append(r)
       elif xmin >= cond:
           false_ranges.append(r)
       else:
           true_range = dict(**r)
           true_range[x] = (xmin, cond-1)
           true_ranges.append(true_range)
           false_range = dict(**r)
           false_range[x] = (cond, xmax)
           false_ranges.append(false_range)
       if true == 'A':
           ret += true_ranges
       elif true == 'R':
           pass
       else:
           ret += process(true, true_ranges)
       if false == 'A':
           ret += false_ranges
       elif false == 'R':
           pass
       else:
           ret += process(false, false_ranges)
    return ret

def part_1():
    s = 0
    for part in parts:
        if process('in', [{k:(v,v) for k, v in part.items()}]):
            s += sum(part.values())
    return s

def part_2():
    ranges = [ {'x' : (1, 4000), 'm' : (1, 4000), 'a' : (1, 4000), 's': (1, 4000) } ]
    
    ranges = process('in', ranges)
    s = 0
    for r in ranges:
        p = 1
        for v in r.values():
            p *= (v[1] - v[0] + 1)
        s += p
    return s


parts, functions = parse_input(inp)

result_1 = part_1()
print ("Part 1:", result_1)
result_2 = part_2()
print ("Part 2:", result_2)

#submit_result(day, year, 1, result_1)
#submit_result(day, year, 2, result_2)
