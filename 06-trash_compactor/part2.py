from math import prod


# lines = [x for x in open("example.txt").read().split('\n') if len(x) > 0]
lines = [x for x in open("input.txt").read().split('\n') if len(x) > 0]

count = 0
col = list()

ops = [l for l in lines.pop() if l != ' ']
ops.reverse()


while len(lines[0]) > 0:

    col.append([l[-1] for l in lines if l[-1] != ' '])
    new_lines = [l[:-1] for l in lines]

    lines = new_lines.copy()
    col = ["".join(c) for c in col]


while len(col) > 0:
    if '' in col:
        cur = col.index('')
    else:
        cur = len(col)

    op = ops.pop(0)
    vals = [int(c) for c in col[:cur]]

    if op == '*':
        count += prod(vals)
    else:
        count += sum(vals)

    col = col[cur+1:]

print(f"Answer: {count}")
