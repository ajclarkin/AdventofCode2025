# input = [x for x in open('example.txt').read().split('\n') if len(x) > 0]
input = [x for x in open('input.txt').read().split('\n') if len(x) > 0]

pos = 50
count = 0

for i in input:
    dir = -1 if i[0] == 'L' else 1
    value = int(i[1:])
    
    pos += dir * value 
    pos = pos % 100

    if pos == 0:
        count += 1

print(f"Answer: {count}")
