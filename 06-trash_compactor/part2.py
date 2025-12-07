from math import prod


# lines = [x for x in open("example.txt").read().split('\n') if len(x) > 0]
lines = [list(x.split()) for x in open("input.txt").read().split('\n') if len(x) > 0]

count = 0
col = list()
# print(lines)

ops = [l for l in lines.pop() if l != ' ']
ops.reverse()


while len(lines[0]) > 0:

    # print([e for e in lines])
    col.append([l[-1] for l in lines if l[-1] != ' '])
    new_lines = [l[:-1] for l in lines]

    lines = new_lines.copy()
    col = ["".join(c) for c in col]

# print(col, ops)

while len(col) > 0:
    # print(f"Col: {col}")
    if '' in col:
        cur = col.index('')
    else:
        cur = len(col)

    op = ops.pop(0)
    # print(col[:cur])
    vals = [int(c) for c in col[:cur]]

    if op == '*':
        count += prod(vals)
    else:
        count += sum(vals)

    col = col[cur+1:]

print(f"Answer: {count}")
