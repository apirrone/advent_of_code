data = open("input.txt", 'r').read().split('\n')[:-1]

def unwrap(p):
    return set([a for a in range(p[0], p[1]+1)])

def any_overlap(pair):
    return bool(set(unwrap(pair[0])) & set(unwrap(pair[1])))

nb = 0

for d in data:
    pair = [list(map(int, p.split('-'))) for p in d.split(',')]
    
    if any_overlap(pair):
        nb += 1

print(nb)
