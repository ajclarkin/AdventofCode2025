from math import prod


# lines = [list(x.split()) for x in open("example.txt").read().split('\n') if len(x) > 0]
lines = [list(x.split()) for x in open("input.txt").read().split('\n') if len(x) > 0]

count = 0
groups = list()

# Ops is read forwards, the number groups are popped (backwards), so reverse it to match
ops = lines.pop()
ops.reverse()


while(len(lines[0]) > 0):
    groups.append([int(e.pop()) for e in lines])

for i, grp in enumerate(groups):
    if ops[i] == '*':
        count += prod(grp)
    else:
        count += sum(grp)


print(F"Answer: {count}")
