# input = [x for x in open('example.txt').read().split('\n') if len(x) > 0]
input = [x for x in open('input.txt').read().split('\n') if len(x) > 0]


ranges = list()
numbers = list()
count = set()

for i in input:
    if i.find('-') != -1:
        ranges.append(list(map(int, i.split('-'))))
    else:
        numbers.append(int(i))



for n in numbers:
    for min, max in ranges:
        if min <= n <= max:
            count.add(n)

print(f"Answer: {len(count)}")

