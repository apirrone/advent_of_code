print(sum([(3 if a==b else (6 if (a, b) in [(1,2), (2,0), (0,1)] else 0)) + b+1 for (a, b) in [(lambda a, b : (a-65, b-88))(*map(ord, d.split(' '))) for d in open("input.txt", 'r').read().split('\n')[:-1]]]))


