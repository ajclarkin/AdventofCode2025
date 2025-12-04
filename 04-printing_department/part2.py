# input = [x for x in open('example.txt').read().split('\n') if len(x) > 0]
input = [x for x in open('input.txt').read().split('\n') if len(x) > 0]

list_rolls = list()
to_remove = list()

search = [(r, c) for r in (-1, 0, 1) for c in (-1, 0, 1)]
search.remove((0, 0))

count = 0

for rownum, row in enumerate(input):
    for colnum, char in enumerate(row):
        if char == "@":
            list_rolls.append((rownum, colnum))

while (True):
    for roll in list_rolls:
        adj = 0

        roll_r, roll_c = roll
        for r, c in search:
            if (roll_r + r, roll_c + c) in list_rolls:
                adj += 1

        if adj < 4:
            to_remove.append(roll)
            count += 1

    print(f"To remove: {len(to_remove)}")
    if len(to_remove) > 0:
        to_remove_working = to_remove.copy()
        for rem in to_remove_working:
            list_rolls.remove(rem)
            to_remove.remove(rem)
    else:
        break

print(f"Answer: {count}")
