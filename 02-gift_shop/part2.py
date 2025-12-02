# input = [x for x in open('example.txt').read().split(',') if len(x) > 0]
input = [x for x in open('input.txt').read().split(',') if len(x) > 0]


count = 0
for i in input:
    start, end = map(int, i.split('-'))

    for j in range(start, end+1):
        j_str = str(j)
        j_len = len(j_str)

        # An AOC trick that won't get pickled up by me methodology
        if j_len == 1:
            continue

        if j_len % 2 != 0:
            lcv_range = int(j_len/2) + 1
        else:
            lcv_range = int(j_len/2)


        for lcv in range(lcv_range):
            testing = lcv + 1
            if j_str[:testing] * (int(j_len / testing)) == j_str:
                count += j
                break

print(f"Answer: {count}")
