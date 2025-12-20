from math import prod
from itertools import combinations


def GetSquaredDist(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2


# Lines will be a list of tuples, each (x, y, z) coordinates
# lines = [tuple(map(int, x.split(','))) for x in open('example.txt').read().split('\n') if len(x) > 0]
lines = [tuple(map(int, x.split(','))) for x in open('input.txt').read().split('\n') if len(x) > 0]

point_count = len(lines)
shortest = dict()
combos = combinations(lines, 2)

# Find all the pairs that can be made
for c in combos:
    dist = GetSquaredDist(*c)
    shortest[dist] = c

# Reverse sort the pairs by distance (keys) for efficiency when popping
shortest_keys = sorted(list(shortest.keys()), reverse=True)


# Now build circuits adding one pair at a time and then joining eveything that can be joined before adding the next pair.
v1, v2 = shortest[shortest_keys.pop()]
circuits = [{v1, v2}]
used = {v1, v2}

while len(used) != point_count or len(circuits) > 1:
    if len(shortest_keys) == 0:
        break
    v1, v2 = shortest[shortest_keys.pop()]
    used.update({v1, v2})
    circuits.append({v1, v2})
    

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

print(f"Coordinates: {v1}, {v2}")
print(f"Answer: {v1[0] * v2[0]}")
