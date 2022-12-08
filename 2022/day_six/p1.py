data = open("input.txt", 'r').read()
print(data)

def allDiff(substr):
    for i in range(len(substr)):
        a = substr[i]
        for j in range(i+1, len(substr)):
            b = substr[j]
            if a == b:
                return False

    return True

for i in range(0, len(data)-3):
    substr = data[i:i+4]
    val = allDiff(substr)
    if val:
        print(i+4, substr)
        exit()
