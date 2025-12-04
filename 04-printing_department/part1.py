# input = [x for x in open('example.txt').read().split('\n') if len(x) > 0]
input = [x for x in open('input.txt').read().split('\n') if len(x) > 0]

list_rolls= list()
search = [(r, c) for r in (-1, 0, 1) for c in (-1, 0, 1)]
search.remove((0, 0))

count = 0

for rownum, row in enumerate(input):
    for colnum, char in enumerate(row):
        if char == "@":
            list_rolls .append((rownum, colnum))

for roll in list_rolls:
    adj = 0

    roll_r, roll_c = roll
    for r, c in search:
        if (roll_r + r, roll_c + c) in list_rolls:
            adj += 1

    if adj < 4:
        count += 1

print(f"Answer: {count}")
