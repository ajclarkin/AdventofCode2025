from itertools import combinations

# points = [(int(a), int(b)) for line in open('example.txt') for a, b in [line.split(',')]]
points = [(int(a), int(b)) for line in open('input.txt') for a, b in [line.split(',')]]


def CalcArea(p1, p2):
    w = abs(p2[0] - p1[0]) + 1
    h = abs(p2[1] - p1[1]) + 1
    return w * h


combos = list(combinations(points, 2))
areas = [CalcArea(*c) for c in combos]

print(max(areas))

