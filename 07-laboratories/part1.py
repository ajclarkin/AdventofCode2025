# lines = [x for x in open('example.txt').read().split('\n')]
lines = [x for x in open("input.txt").read().split("\n")]

positions = {lines.pop(0).index("S")}
count = 0

for l in lines:
    splitters = [i for i, char in enumerate(l) if char == "^"]
    unchanged = {p for p in positions if p not in splitters}
    changed = [p for p in positions if p in splitters]
    count += len(changed)

    changed_down = [c - 1 for c in changed if c > 0]
    changed_up = [c + 1 for c in changed if c < len(lines[0])]

    unchanged.update(changed_down)
    unchanged.update(changed_up)

    old_pos_len = len(positions)
    positions = unchanged.copy()

    # print(l, splitters, positions)
print(f"Answer: {count}")
