# input = [x for x in open('example.txt').read().split('\n') if len(x) > 0]
input = [x for x in open('input.txt').read().split('\n') if len(x) > 0]

count = 0

for i in input:
    line = [int(l) for l in i]
    lastpos = 0
    digits = []

    for i in range(12):
        end_range = (-11 + i) if i < 11 else None

        d = max(line[lastpos:end_range])
        d_pos = line[lastpos:end_range].index(d)
        lastpos = d_pos + lastpos + 1
        digits.append(d)

    digits_str = map(str, digits)
    num = int("".join(digits_str))
    count += num 


print(f"Answer: {count}")
