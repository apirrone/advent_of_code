import numpy as np
data = open("input.txt", 'r')#.read()#.split('\n')[:-1]

lines = data.readlines()

# cols = 3
# rows = 3
cols = 9
rows = 8

def move(stacks, movestr):
    tmp = movestr.split(' ')
    nb = int(tmp[1])
    fr = int(tmp[3])
    to = int(tmp[5])

    stacks[to-1] += stacks[fr-1][-nb:]
    stacks[fr-1] = stacks[fr-1][:-nb]

    return stacks



stacks = []
actions = []
for i, line in enumerate(lines):
    if i < rows:
        a = [line[i:i+4] for i in range(0, len(line), 4)]
        a = [aa.strip('\n').strip('[').strip('] ') for aa in a]

        stacks.append(a)
    elif i > rows+1:
        actions.append(line.strip('\n'))


stacks = [s[::-1] for s in np.array(stacks).T]

sstacks = []
for s in stacks:
    tmp = []
    for ss in s:
        if ss != '':
            tmp.append(ss)

    sstacks.append(tmp)

for action in actions:
    move(sstacks, action)

str = ''
for stack in sstacks:
    str+=stack[-1]

print(str)

