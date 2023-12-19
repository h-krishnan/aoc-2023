import os
import requests

def toArray(lst, *args):
    if len(args) == 0:
        return lst
    N, *args = args
    return toArray([toArray(lst[i:i+N]) for i in range(0, len(lst), N)], *args)

def makeArray(value, *args):
    if len(args) == 1:
        if isinstance(value, (set, list)):
            value = value.__class__(x for x in value)
        return [value]*args[0]
    N, *args = args
    return list(makeArray(value, *args)[:] for x in range(N))

def array2DToDict(array):
    ret = {}
    for x, r in enumerate(array):
        for y, c in enumerate(r):
            ret[(x, y)] = c
    return ret, x+1, y+1

def transpose2d(A):
    return [list(x) for x in zip(*A)]

from collections import namedtuple
Point = namedtuple('Point', ('x', 'y'))
class Pt(Point):
    def __add__(self, rhs):
        return Pt(self.x + rhs[0],
                  self.y + rhs[1])

    def __sub__(self, rhs):
        return Pt(self.x - rhs[0],
                  self.y - rhs[1])

    def __mul__(self, rhs):
        return Pt(self.x*rhs, self.y*rhs)

    def __div__(self, rhs):
        return Pt(self.x/rhs, self.y/rhs)


    @property
    def pt(self):
        return (self.x, self.y)

    def dir(self):
        return Pt(self.x/(abs(self.x) if self.x != 0 else 1),
                  self.x/(abs(self.y) if self.y != 0 else 1))

    def move(self, dir, d = 1):
        return Pt(self.x + dir[0]*d,
                  self.y + dir[1]*d)

    def n(self, d = 1):
        return Pt(self.x, self.y + d)

    def s(self, d = 1):
        return Pt(self.x, self.y - d)

    def e(self, d = 1):
        return Pt(self.x + d, self.y)

    def w(self, d = 1):
        return Pt(self.x - d, self.y)

    def ne(self, d = 1):
        return Pt(self.x + d, self.y + d)

    def nw(self, d = 1):
        return Pt(self.x - d, self.y + d)

    def se(self, d = 1):
        return Pt(self.x + d, self.y - d)

    def sw(self, d = 1):
        return Pt(self.x - d, self.y - d)

    def gridNbrs(self, bl = None, tr = None):
        ret = [self.n(), self.s(), self.e(), self.w()]
        if tr:
            return [x for x in filter(lambda x: x.inrange(bl, tr), ret)]
        return ret

    def allNbrs(self, bl = None, tr = None):
        ret = [self.n(), self.ne(), self.e(), self.se(), self.s(), self.sw(), self.w(), self.nw()]
        if tr:
            return [x for x in filter(lambda x: x.inrange(bl, tr), ret)]
        return ret
    def inrange(self, bl, tr):
        return bl.x <= self.x <= tr.x and bl.y <= self.y <= tr.y

dir1 = Pt(0, 0).gridNbrs()
dir2 = Pt(0, 0).allNbrs()

def turnRight(d):
    return dir1[ (dir1.index(d) + 1) % 4 ]

def turnLeft(d):
    return dir1[ (dir1.index(d) - 1) % 4 ]


from queue import PriorityQueue  # essentially a binary heap


def dijkstra_p(start, start_wt, goal, G):
    """ Uniform-cost search / dijkstra """
    visited = set()
    cost = {start: start_wt}
    parent = {start: None}
    todo = PriorityQueue()

    todo.put((0, start))
    while todo:
        while not todo.empty():
            _, vertex = todo.get()  # finds lowest cost vertex
            # loop until we get a fresh vertex
            if vertex not in visited: break
        else:  # if todo ran out
            break  # quit main loop
        visited.add(vertex)
        if vertex == goal:
            break
        for distance, neighbor in G(vertex):
            if neighbor in visited: continue  # skip these to save time
            old_cost = cost.get(neighbor, float('inf'))  # default to infinity
            new_cost = cost[vertex] + distance
            if new_cost < old_cost:
                todo.put((new_cost, neighbor))
                cost[neighbor] = new_cost
                parent[neighbor] = vertex

    return parent, visisted

import heapq
def dijkstra(startNode, startWt, targetNode, nbrFn):
    """

    :param startNode: should be hashable
    :param startWt: starting weight: typically zero
    :param targetNode: node to be reached
    :param nbrFn(p): An fn returning neighbors of p  [ (wt1, nb1), (wt2, nb2) ...]
    :return: shortedRoute, solvedRoutes
    """
    todo = []
    heapq.heapify(todo)
    heapq.heappush(todo, (startWt, startNode, None))
    remaining = {}
    remaining[startNode] = startWt
    sptset = {}
    while remaining:
        #print ("remaining = ", len(remaining))
        wt, p, parent = heapq.heappop(todo)
        if p in sptset: continue

        sptset[p] = (wt, parent)
        if (callable(targetNode) and targetNode(p)) or p == targetNode:
            break
        del remaining[p]
        for v, n in nbrFn(p):
            t = v + wt
            found = sptset.get(n)
            #if found and found[0] > t:
            #    print ("oops", n, t, found)
            if found: continue
            nv = remaining.get(n)
            if not nv or nv > t:
                remaining[n] = t
                heapq.heappush(todo, (t, n, p))

    return wt, p, sptset[p], sptset

session_id = os.getenv("AOC_SESSIONID")
user_agent = os.getenv("AOC_USERAGENT")

_headers = {'User-Agent': user_agent}
def get_input(day, year):
    uribase = r"https://adventofcode.com/" + str(year) + '/day/' + str(day)
    uri = uribase + r"/input"
    try:
        inp = open(str(day) + r'.txt').read()
    except Exception:
        inp = requests.get(uri, cookies=dict(session=session_id), headers=_headers)
        with open(str(day) + r'.txt', 'w') as f:
            f.write(inp.text)
        inp = inp.text
    return inp

def submit_result(day, year, level, result):
    if result is not None:
        uribase = r"https://adventofcode.com/" + str(year) + '/day/' + str(day)

        response = requests.post(uribase + "/answer", cookies={"session": SESSIONID},
                                 headers=_headers,
                                 data={"level": level, "answer": result})
        if response.ok:
            if "That's the right answer" in response.text:
                print("Success!")
            elif " low" in response.text:
                print("Too low :-(")
            elif " high" in response.text:
                print("Too high :-(")
            else:
                print("Wrong answer :-(")
                print(response.text)
        else:
            print("Response not OK")
            print(response.text)

