from itertools import combinations

# points = [(int(a), int(b)) for line in open('example.txt') for a, b in [line.split(',')]]
points = [(int(a), int(b)) for line in open('input.txt') for a, b in [line.split(',')]]

perimeter = set()
# internal, external = set()


first = points.pop(0)
points.append(first)
c, r = first

for c2, r2 in points:
    if c2 == c:
        diff = 1 if r2 > r else -1
        u = ([(c,i) for i in range(r, r2 + diff, diff)])
        perimeter.update(u)
    else:
        diff = 1 if c2 > c else -1
        u = ([(i,r) for i in range(c, c2 + diff, diff)])
        perimeter.update(u)

    c, r = c2, r2    


min_c = min(perimeter, key=lambda t: t[0])[0]
max_c = max(perimeter, key=lambda t: t[0])[0]
min_r = min(perimeter, key=lambda t: t[1])[1]
max_r = max(perimeter, key=lambda t: t[1])[1]

print(min_c, max_c)
print(min_r, max_r)

# def CheckArea(p1: tuple[int, int], p2: tuple[int, int]) -> None: 
#
#
# combos = combinations(points, 2)
