from itertools import combinations, product

# points = [
#     (int(a), int(b)) for line in open("example.txt") for a, b in [line.split(",")]
# ]
points = [
    (int(a), int(b)) for line in open("input.txt") for a, b in [line.split(",")]
]
# points = [(int(a), int(b)) for line in open('input.txt') for a, b in [line.split(',')]]

perimeter = set()
internal = set()
external = set()

first = points.pop(0)
points.append(first)
c, r = first

for c2, r2 in points:
    if c2 == c:
        diff = 1 if r2 > r else -1
        u = [(c, i) for i in range(r, r2 + diff, diff)]
        perimeter.update(u)
    else:
        diff = 1 if c2 > c else -1
        u = [(i, r) for i in range(c, c2 + diff, diff)]
        perimeter.update(u)

    c, r = c2, r2


limits = {
    "min_c": min(perimeter, key=lambda t: t[0])[0],
    "max_c": max(perimeter, key=lambda t: t[0])[0],
    "min_r": min(perimeter, key=lambda t: t[1])[1],
    "max_r": max(perimeter, key=lambda t: t[1])[1],
}

print(limits)


def isPointInternal(
    point: tuple[int, int], internal: set, external: set, perimeter: set, limits: dict
):
    if point in internal or point in perimeter:
        return True
    if (
        point in external
        or point[0] < limits["min_c"]
        or point[0] > limits["max_c"]
        or point[1] < limits["min_r"]
        or point[1] > limits["max_r"]
    ):
        
        return False

    c = point[0]
    r = point[1]

    points_to_check = {(x, r) for x in range(c + 1, limits["max_c"] + 1)}
    perimeter_count = len(points_to_check & perimeter)

    if perimeter_count % 2 == 1:
        internal.add(point)
        # print(f"point {point} is internal")
        return True
    else:
        external.add(point)
        return False



def CalcArea(p1, p2):
    w = abs(p2[0] - p1[0]) + 1
    h = abs(p2[1] - p1[1]) + 1
    return w * h



def isValidArea(p1, p2):
    cols = [p1[0], p2[0]]
    rows = [p1[1], p2[1]]

    c_vals = [c for c in range(min(cols), max(cols)+1)]
    r_vals = [r for r in range(min(rows), max(rows)+1)]

    print(f"Checking area {p1} to {p2}\tcols: {min(cols)} to {max(cols)+1}\trows: {min(rows)} to {max(rows)+1}")
    all_points = list(product(c_vals, r_vals))
    # if all(isPointInternal(p, internal, external, perimeter, limits) for p in all_points):

    validity = [isPointInternal(p, internal, external, perimeter, limits) for p in all_points]

    if all(validity):
        area = CalcArea(p1, p2)
    else:
        area = 0

    # for current_p in all_points:
    #     if isPointInternal(current_p, internal, external, perimeter, limits):
    #         continue
    # else:
    #     print("Invalid")
    #     return 0
    #
    # area = CalcArea(p1, p2)
    return area



combos = combinations(points, 2)
areas = [isValidArea(*c) for c in combos]

print(f"Max area {max(areas)}")





