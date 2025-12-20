from math import comb, prod
from itertools import combinations
from functools import cache
from collections import Counter

def GetSquaredDist(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2


# Lines will be a list of tuples, each (x, y, z) coordinates
# lines = [tuple(map(int, x.split(','))) for x in open('example.txt').read().split('\n') if len(x) > 0]
lines = [tuple(map(int, x.split(','))) for x in open('input.txt').read().split('\n') if len(x) > 0]
MAX_PAIRS = 1000


# First consider each possible pairing of points:
#   - if we don't have the required number of pairs saved then save it (add to shortest)
#   - otherwise replace the pair with longest distance in dict if this is shorter
#   - dict shortest is of format: sortest[distance] = (point1, point2)

shortest = dict()
combos = combinations(lines, 2)

for c in combos:
    dist = GetSquaredDist(*c)
    if len(shortest) < MAX_PAIRS:
        shortest[dist] = c
    elif dist < max(shortest):
        shortest.pop(max(shortest))
        shortest[dist] = c


# Now make a list of circuits, each stored as a set.
# Try every combination of sets to see if they should be joined: if so then remove the two circuits and add the joined
# circuits instead.
# Process stops when the list of circuits doesn't get shorter - that is, there are no more unions to make.
circuits = [set(v) for v in shortest.values()]

while True:
    prev_circuit_len = len(circuits)
    circ_combos = combinations(circuits, 2)
    for s1, s2 in circ_combos:
        if s1.isdisjoint(s2):
            continue
        else:
            new_circuit = s1.union(s2)
            circuits.remove(s1)
            circuits.remove(s2)
            circuits.append((new_circuit))
            break
        
    if len(circuits) == prev_circuit_len:
        break


# circuits is a list of sets. Order the list by the length of the set descending. Take the first 3 and add to a list.
sort_by_len = list(map(len, sorted(circuits, key=lambda c: len(c), reverse=True)[:3]))
print(prod(sort_by_len))
