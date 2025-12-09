# lines = [x for x in open('example.txt').read().split('\n') if len(x) > 0]
lines = [x for x in open("input.txt").read().split("\n") if len(x) > 0]

start = lines[0].index("S")
print(lines)
maxlen = len(lines)
print(maxlen)
splitters = []

count = 0

def nextrow(cur_r, cur_pos, tracker):
    # print(f"cur_r: {cur_r}, cur_pos: {cur_pos}, tracker: {tracker}")
    # input()
    tracker.append(cur_pos)
    cur_r += 1

    # print(f"Char to read: {lines[cur_r]}  |  {lines[cur_r][cur_pos]}")

    if cur_r == maxlen:
        if tuple(tracker) not in routes:
            routes.add(tuple(tracker))
            print(len(routes))
        # print("Routes: ", routes)
    else:
        if lines[cur_r][cur_pos] == '^':
            # print('Found ^')
            nextrow(cur_r, cur_pos-1, tracker)
            nextrow(cur_r, cur_pos+1, tracker)
        else:
            # print('Not found ^')
            nextrow(cur_r, cur_pos, tracker)
    tracker.pop()

cur_r = 0
cur_pos = start
routes = set()
tracker = list()

nextrow(cur_r, cur_pos, tracker)
print(routes)
print(len(routes))
