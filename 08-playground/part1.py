from math import prod
from itertools import combinations
from functools import cache
from collections import Counter

def GetSquaredDist(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2

lines = [tuple(map(int, x.split(','))) for x in open('example.txt').read().split('\n') if len(x) > 0]
lines = [tuple(map(int, x.split(','))) for x in open('input.txt').read().split('\n') if len(x) > 0]
MAX_PAIRS = 1000

shortest = dict()
combos = combinations(lines, 2)

for c in combos:
    dist = GetSquaredDist(*c)
    if len(shortest) < MAX_PAIRS:
        shortest[dist] = c
    elif dist < max(shortest):
        shortest.pop(max(shortest))
        shortest[dist] = c

circuits = [set()]
for a, b in shortest.values():
    for c in circuits:
        if a in c or b in c:
            c.add(a)
            c.add(b)
            break
    else:
        circuits.append({a, b})


# for c in circuits:
#     print(len(c))

# circuits is a list of sets. Order the list by the length of the set descending. Take the first 3 and add to a list.
sort_by_len = list(map(len, sorted(circuits, key=lambda c: len(c), reverse=True)[:3]))
print(sort_by_len)
print(prod(sort_by_len))
