# input = [x for x in open('example.txt').read().split('\n') if len(x) > 0]
input = [x for x in open('input.txt').read().split('\n') if len(x) > 0]

prevpos = 50
count = 0

for i in input:
    dir = -1 if i[0] == 'L' else 1
    value = int(i[1:])
    
    pos = prevpos + (dir * value)
    # pos = pos % 100

    count +=abs(prevpos//100 - pos//100) 

    prevpos = pos

print(f"Answer: {count}")
