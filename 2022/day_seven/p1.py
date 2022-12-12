lines = open("input.txt", 'r').readlines()
# print(lines)

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Dir:
    def __init__(self, name, path):
        self.name  = name

        self.dirs  = []
        self.files = []
        self.path  = path + '/' + self.name

    def getPath(self):
        return self.path

    def show(self):
        for d in self.dirs:
            print("dir", d.name)

        for f in self.files:
            print(f.size, f.name)

    def addFile(self, name, size):
        if not self.fileExists(name):
            self.files.append(File(name, size))

    def addDir(self, name, path):
        if not self.dirExists(name):
            self.dirs.append(Dir(name, path))

    def fileExists(self, name):
        for file in self.files:
            if name == file.name:
                return True

        return False

    def dirExists(self, name):
        for dir in self.dirs:
            if name == dir.name:
                return True

        return False

    def getSubDirFromName(self, name):
        for dir in self.dirs:
            if dir.name == name:
                return dir

        return None
        # return "root"


class FileSystem:
    def __init__(self):
        self.root       = Dir('', '/')
        self.currentDir = self.root
        self.prevDir    = self.root

    def cd(self, arg):  

        if arg == "..":
            self.currentDir = self.prevDir
        elif arg == '/':
            self.currentDir = self.root
        else:
            self.prevDir    = self.currentDir
            dir             = self.currentDir.getSubDirFromName(arg)

            if dir == "root":
                self.currentDir = self.root
            else:
                self.currentDir = dir


    def ls(self):
        self.currentDir.show()

    def mkdir(self, name):
        self.currentDir.addDir(name, self.currentDir.getPath())

    def touch(self, name, size):
        self.currentDir.addFile(name, size)

    def pwd(self):
        print(self.currentDir.getPath())




fs = FileSystem()

for line in lines:
    line = line.strip('\n')
    print("path :", fs.pwd())
    print(line)


    # Command
    if line[0] == '$':
        tmp = line.split(' ')
        cmd = tmp[1]
        if cmd == "cd":
            arg = tmp[2]
            fs.cd(arg)
        elif cmd == "ls":
            pass
    else:
        tmp = line.split(' ')
        if tmp[0] == "dir":
            name = tmp[1]
            fs.mkdir(name)
        else:
            tmp  = line.split(' ')
            size = int(tmp[0])
            name = tmp[1]
            fs.touch(name, size)


# fs.cd('/')
# fs.mkdir("aze")
# fs.mkdir("azeee")
# fs.mkdir("azeeeeee")
# fs.cd("azeee")
# fs.mkdir("bbz")
# fs.mkdir("aaaa")
# fs.cd("..")
# fs.cd("aze")
# fs.mkdir("pp")
# fs.touch("alalall", 123)
# fs.cd("..")
# fs.ls()