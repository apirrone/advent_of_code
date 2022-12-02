data = list(map(int, open("input.txt", 'r').read().split('\n')[:-1]))

sums = []
incr = 0
for i in range(1, len(data)-1):
    sums.append(sum([data[i-1], data[i], data[i+1]]))
    if len(sums) > 1:
        if sums[-1] > sums[-2]:
            incr += 1

print(incr)

