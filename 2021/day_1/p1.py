data = list(map(int, open("input.txt", 'r').read().split('\n')[:-1]))

incr = 0
for i in range(1, len(data)):
    if data[i] > data[i-1]:
        incr += 1

print(incr)