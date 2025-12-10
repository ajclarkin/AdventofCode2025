from functools import cache

# lines = [x for x in open('example.txt').read().split('\n') if len(x) > 0]
lines = [x for x in open("input.txt").read().split("\n") if len(x) > 0]

@cache
def nextrow(cur_r, cur_pos):
    cur_r += 1

    if cur_r == maxlen:
        return 1
    else:
        if lines[cur_r][cur_pos] == '^':
            return nextrow(cur_r, cur_pos-1) + nextrow(cur_r, cur_pos+1)
        else:
            return nextrow(cur_r, cur_pos)


cur_pos = lines[0].index("S")
cur_r = 0
maxlen = len(lines)

count = nextrow(cur_r, cur_pos)

print(f"Answer: {count}")
