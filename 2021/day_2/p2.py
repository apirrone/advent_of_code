data = open("input.txt", 'r').read().split('\n')[:-1]
horiz = 0
depth = 0
aim   = 0
for d in data:
    dir, val = d.split(' ')
    if dir == "forward":
        horiz += int(val)
        depth += (int(val)*aim)
    elif dir == "up":
        aim -= int(val)
    else:
        aim += int(val)

print(depth, horiz, depth*horiz)