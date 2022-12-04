data = open("input.txt", 'r').read().split('\n')[:-1]

def priority(char):
    if char.islower():
        return ord(char)-96
    else:
        return ord(char)-64 + 26

def common(r1, r2, r3):
    for rr1 in r1:
        for rr2 in r2:
            if rr1 == rr2:
                for rr3 in r3:
                    if rr2 == rr3:
                        return rr3

commons = []
for i in range(1, len(data)-1, 3):
    r1 = data[i-1]
    r2 = data[i]
    r3 = data[i+1]
    commons.append(common(r1, r2, r3))


res = sum(list(map(priority, commons)))
print(res)