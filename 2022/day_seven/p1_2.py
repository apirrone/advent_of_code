lines = open("input.txt", 'r').readlines()

dirs = {}

dirStack = []

def currentDir():
    if len(dirStack) == 0:
        return "/"
    else:
        return dirStack[-1]

for line in lines:
    line = line.strip('\n')
    tmp = line.split(' ')
    if tmp[0] == '$':
        if tmp[1] == "cd":
            if tmp[2] != "..":
                dirStack.append(tmp[2])
                dirs[currentDir()] = {"path":dirStack.copy(), "size" : 0}
            else:
                dirStack = dirStack[:-1]
        elif tmp[1] == "ls":
            pass
    elif tmp[0] == "dir":
        pass
    else: # files
        fileSize = int(tmp[0])
        dirs[currentDir()]["size"] += fileSize

for k, v in dirs.items():
    print(k, v)

dirSizes = {}
pathsLengths = {}
for k, v in dirs.items():
    pathsLengths[k] = len(v["path"])
    dirSizes[k] = 0


dirsByPathSize = sorted(pathsLengths, reverse=True)

for dir in dirsByPathSize:
    dirSize = dirs[dir]["size"]
    path = dirs[dir]["path"]

    for i in range(len(path)-1, -1, -1):
        dirSizes[path[i]] += dirSize

size = 0
for k, s in dirSizes.items():
    if s <= 100000:
        size += s

print(size)


# print(list(sorted(pathsLengths.items(), key=lambda item: item[1], reverse=True)))



