data = open("input.txt", 'r').read().split('\n')[:-1]

def unwrap(pair):
    return set([a for a in range(pair[0][0], pair[0][1]+1)]), set([a for a in range(pair[1][0], pair[1][1]+1)])

def full_overlap(pair):
    p1, p2 = unwrap(pair)
    
    return p1.issubset(p2) or p2.issubset(p1)

nb = 0

for d in data:
    pair = [list(map(int, p.split('-'))) for p in d.split(',')]

    if full_overlap(pair):
        nb += 1

print(nb)
