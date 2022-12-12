import numpy as np

# [[ True  True  True  True  True]
#  [ True  True  True False  True]
#  [ True False False  True  True]
#  [ True False  True False  True]
#  [ True  True  True  True  True]]


data = open("input.txt", 'r').readlines()

for i in range(len(data)):
    data[i] = data[i].strip('\n')

forest = np.zeros((len(data), len(data[0]))) # (i, j)

for i in range(len(data)):
    for j in range(len(data[i])):
        forest[i][j] = data[i][j]

print(forest)
fromLeft  = np.zeros(forest.shape, dtype=bool)
fromRight = np.zeros(forest.shape, dtype=bool)
fromTop   = np.zeros(forest.shape, dtype=bool)
fromDown  = np.zeros(forest.shape, dtype=bool)

def computeMaskSlice(slice):
    maskSlice = np.ones(len(slice))
    for k in range(1, len(slice)):
        for l in range(k-1, -1, -1):
            if slice[l] >= slice[k]:
                maskSlice[k] = 0
        # if maskSlice[k-1] and slice[k-1] < slice[k]:
        #     maskSlice[k] = 1

    return maskSlice


for i in range(len(forest)):
    slice        = forest[i]

    fromLeft[i] = computeMaskSlice(slice)

print("FromLeft :")
print(fromLeft)

for i in range(len(forest)):
    slice        = list(reversed(forest[i]))

    fromRight[i] = list(reversed(computeMaskSlice(slice)))

print("FromRight :")
print(fromRight)

for j in range(len(forest[0])):
    slice        = forest[:, j]

    fromTop[:, j] = computeMaskSlice(slice)


print("FromTop :")
print(fromTop)

for j in range(len(forest[0])):
    slice        = list(reversed(forest[:, j]))

    fromDown[:, j] = list(reversed(computeMaskSlice(slice)))


print("fromDown :")
print(fromDown)
print("==========")

mask = fromLeft | fromRight | fromTop | fromDown
print(mask)
print(sum(sum(mask)))
# print(np.bitwise_or(np.array(fromLeft), np.array(fromRight)))

# mask = np.bitwise_or(fromLeft,np.bitwise_or(np.bitwise_or(fromTop, fromDown), fromRight))

# print(mask)
