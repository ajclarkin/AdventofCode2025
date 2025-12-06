# input = [x for x in open('example.txt').read().split('\n') if len(x) > 0]
input = [x for x in open('input.txt').read().split('\n') if len(x) > 0]
from itertools import combinations

ranges = set()

# This gives us a set of tuples containing all the ranges
for i in input:
    if i.find('-') != -1:
        ranges.add(tuple(map(int, i.split('-'))))


while True:
    ranges_copy = ranges.copy()
    
    # Work through each pair of ranges.
    # If a pair intersect create a new range and discard the old two, then restart combinations()
    for combo in combinations(ranges_copy, 2):
        l1, h1 = combo[0]
        l2, h2 = combo[1]

        l1, h1 = combo[0]

        # Do they overlap
        if (
            (l1 < l2 and l2 <= h1 <= h2) or
            (l2 < l1 and l1 <= h2 <= h1) or
            (l1 <= l2 and h1 >= h2) or
            (l2 <= l1 and h2 >= h1)
        ):
            low = min(l1, l2)
            high = max(h1, h2)
            ranges.remove(combo[0])
            ranges.remove(combo[1])
            ranges.add((low, high))

            break

    if ranges == ranges_copy:
        break


count = 0
for r in ranges:
    count += r[1] - r[0] + 1

print(f"Answer: {count}")
