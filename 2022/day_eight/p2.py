import numpy as np

data = open("input.txt", 'r').readlines()

for i in range(len(data)):
    data[i] = data[i].strip('\n')

forest = np.zeros((len(data), len(data[0])))

for i in range(len(data)):
    for j in range(len(data[i])):
        forest[i][j] = data[i][j]

print(forest)

def scenic_score(forest, i, j):
    horizSice = forest[i, :]
    vertSlice = forest[:, j]

    leftSlice = list(reversed(horizSice[:j]))
    rightSlice = horizSice[j+1:]
    upSlice = list(reversed(vertSlice[:i]))
    downSlice = vertSlice[i+1:]

    val = forest[i][j]

    # print(leftSlice)
    # print(rightSlice)
    # print(upSlice)
    # print(downSlice)

    scores = []
    print("VAL : ", val)
    for slice in [leftSlice, rightSlice, upSlice, downSlice]:
        score = 0
        for i in range(len(slice)):
            if slice[i] < val:
                score += 1
            else:
                score += 1
                break

        scores.append(score)

    
    return np.prod(scores)

scores = []
for i in range(len(forest)):
    for j in range(len(forest[i])):
        scores.append(scenic_score(forest, i, j))

print(max(scores))
