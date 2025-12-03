# input = [x for x in open('example.txt').read().split('\n') if len(x) > 0]
input = [x for x in open('input.txt').read().split('\n') if len(x) > 0]


count = 0
for i in input:
    digits = sorted(list(i), reverse=True)[:2]

    if i.find(digits[0]) == len(i)-1:
        digits.reverse()
        count += int("".join(digits))
    else:
        digitpos = i.find(digits[0])
        digits[1] = max(list(i)[digitpos+1:])

        count += int("".join(digits))

print(f"Answer: {count}")
