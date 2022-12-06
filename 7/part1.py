import sys, re, functools

class File(object):
  def __init__(self, parent, name, size):
    self.parent = parent
    self.name = name
    self._size = size

  def size(self):
    return self._size

  def __repr__(self):
    return "%s(%s)" % (self.name, self._size)

class Dir(object):
  def __init__(self, parent, name):
    self.parent = parent
    self.name = name
    self.files = []

  def addFile(self, file):
    self.files.append(file)

  def size(self):
    return functools.reduce(lambda x,y: x + y.size(), self.files, 0)

  def getFile(self, name):
    for file in self.files:
      if file.name == name:
        return file
    return None

  def __repr__(self):
    return "%s(%s)" % (self.name, self.files)

  def format(self, level=0):
    indent = " " * level
    retval = indent + self.name + "\n"
    for file in self.files:
      if isinstance(file, Dir):
        retval += file.format(level+1)
      else:
        retval += indent + " " + repr(file) + "\n"
    return retval

rootDir = Dir(None, "/")
target = None

for line in sys.stdin:
  if line[0:5] == "$ cd ":
    targetStr = line[5:-1]
    if targetStr == '/':
      target = rootDir
    elif targetStr == '..':
      target = target.parent
    elif target.getFile(targetStr) != None:
      target = target.getFile(targetStr)
    else:
      newTarget = Dir(target, targetStr)
      target.addFile(newTarget)
      target = newTarget
  elif line[0:4] == "$ ls":
    pass
  elif line[0:4] == "dir ":
    #ls entry for a dir
    dirName = line[4:-1]
    newDir = Dir(target, dirName)
    target.addFile(newDir)
  else:
    m = re.search(r"([0-9]+) ([a-zA-Z0-9.]+)", line)
    if m==None:
      print("ERROR parsing %s" % line)
      continue
    size = int(m.group(1))
    name = m.group(2)

    newFile = File(target, name, size)
    target.addFile(newFile)

totalSize = 0
def answer(file):
  global totalSize
  if isinstance(file, Dir):
    if file.size() < 100000:
      totalSize += file.size()
    for child in file.files:
      answer(child)

answer(rootDir)

print(rootDir.format())
print(totalSize)
