# input = [x for x in open('example.txt').read().split(',') if len(x) > 0]
input = [x for x in open('input.txt').read().split(',') if len(x) > 0]


count = 0
for i in input:
    start, end = map(int, i.split('-'))

    for j in range(start, end+1):
        j_str = str(j)
        j_len = len(j_str)
        
        if j_len % 2 == 0 and j_str[0:int(j_len/2)] == j_str[int(j_len/2):]:
            count += j

print(f"Answer: {count}")
