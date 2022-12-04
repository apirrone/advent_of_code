data = open("test_input.txt", 'r').read().split('\n')[:-1]

def priority(char):
    if char.islower():
        return ord(char)-96
    else:
        return ord(char)-64 + 26

def common(c1, c2):
    for cc1 in c1:
        for cc2 in c2:
            if cc1 == cc2:
                return cc1

commons = []
for d in data:
    c1 = d[:len(d)//2]
    c2 = d[len(d)//2:]

    commons.append(common(d[:len(d)//2], d[len(d)//2:]))


res = sum(list(map(priority, commons)))
print(res)