data = open("input.txt", 'r').read().split('\n')[:-1]
horiz = 0
depth = 0
for d in data:
    dir, val = d.split(' ')
    if dir == "forward":
        horiz += int(val)
    elif dir == "up":
        depth -= int(val)
    else:
        depth += int(val)

print(depth, horiz, depth*horiz)