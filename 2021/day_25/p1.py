import numpy as np

charmap = {'.' : 0, '>' : 1, 'v' : 2}

def downMask(map):
    mask = np.zeros((map.shape[0], map.shape[1])) # i, j -> (137, 139)
    for i in range(map.shape[0]-1):
        line = map[i+1, :]
        mask[i, :] = line==0
    mask[map.shape[0]-1, :] = map[0, :]==0
    return mask

def rightMask(map):
    mask = np.zeros((map.shape[0], map.shape[1])) # i, j -> (137, 139)
    for j in range(map.shape[1]-1):
        line = map[:, j+1]
        mask[:, j] = line==0    
    mask[:, map.shape[1]-1] = map[:, 0]==0
    return mask

lines = open("input.txt", "r").read().split('\n')#[:-1]
map = np.zeros((len(lines), len(lines[0]))) # i, j -> (137, 139)

for i, line in enumerate(lines):
    for j , c in enumerate(line):
        map[i][j] = charmap[c]

step = 1
running = True
while running:
    print("== STEP", step, "==")
    # print(map)
    rightmask = rightMask(map)
    # print("rightmask")
    # print(rightmask)

    couldMoveRight = False
    couldMoveDown  = False

    # right pass
    for i in range(map.shape[0]):
        looped=False
        for j in range(map.shape[1]-1, -1, -1):
            val = map[i][j]
            if val == 1:
                if rightmask[i][j]:
                    couldMoveRight = True
                    if j < map.shape[1]-1:
                        map[i][j+1] = val
                    elif not looped:
                        map[i][0] = val
                        looped=True
                    map[i][j] = 0

    # print("after right")
    # print(map)

    downmask  = downMask(map)
    
    # down pass
    for j in range(map.shape[1]):
        looped = False
        for i in range(map.shape[0]-1, -1, -1):
            val = map[i][j]
            if val == 2:
                if downmask[i][j]:
                    couldMoveDown = True
                    if i < map.shape[0]-1:
                        map[i+1][j] = val
                    elif not looped:
                        map[0][j] = val
                        looped = True
                    map[i][j] = 0

    # print("after down")
    # print(map)

    # input()
    print(couldMoveRight, couldMoveDown)
    print("===")
    # input()

    if not couldMoveRight and not couldMoveDown:
        running = False




    step += 1


