data = open("input.txt", 'r').read().split('\n')[:-1]
win = {0 : 1, 1 : 2, 2 : 0}

score = 0
for d in data:
    a, b = (lambda a, b : (a-65, b-88))(*map(ord, d.split(' ')))
    if b == 0:
        b = dict([list(reversed(a)) for a in list(win.items())])[a]
    elif b == 1:
        b = a
    else:
        b = win[a]
    score += (3 if a==b else (6 if (a, b) in [(1,2), (2,0), (0,1)] else 0)) + b+1
print(score)

    