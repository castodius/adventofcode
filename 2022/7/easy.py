import sys

LIMIT = 10**5
total = 0
total_sizes = []

class Node():
  def __init__(self, name):
    self.name = name
    self.parent = None
    self.children = []
    self.files = []
    self.total_size = 0

  def add_child(self, child):
    child.set_parent(self)
    self.children.append(child)

  def set_parent(self, parent):
    self.parent = parent

  def add_file(self, name, size):
    self.files.append((name, size))

  def sum(self):
    for file in self.files:
      self.total_size += file[1]

    for child in self.children:
      self.total_size += child.sum()

    global total
    if self.total_size <= LIMIT:
      total += self.total_size

    global total_sizes
    total_sizes.append(self.total_size)
    return self.total_size
    

top = Node('/')
curr = top
sys.stdin.readline()

for line in sys.stdin:
  line = line.strip()

  if line == '$ ls':
    continue

  if line == '$ cd ..':
    curr = curr.parent
    continue

  if line.startswith('$ cd'):
    name = line.split(' ')[2]
    n = Node(name)
    curr.add_child(n)
    curr = n
    continue

  if line.startswith('dir '):
    continue

  size, name = line.split(' ')
  size = int(size)
  curr.add_file(name, size)

used = top.sum()
print(total)

free = 7*10**7 - used
needed = 3*10**7 - free
total_sizes.sort()
for value in total_sizes:
  if value < needed:
    continue
  print(value)
  break