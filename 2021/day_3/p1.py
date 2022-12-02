import numpy as np
data = open("input.txt", 'r').read().split('\n')[:-1]

a = np.zeros((len(data), len(data[0]))).T
gamma   = '0b'
epsilon = '0b'
for i, line in enumerate(data):

    a[:, i] = list(map(int, list(line)))

for line in a:
    if np.mean(line) > 0.5:
        gamma   += '1'
        epsilon += '0'
    else:
        gamma   += '0'
        epsilon += '1'
print(gamma, epsilon)
print(int(gamma, 2)*int(epsilon, 2))
