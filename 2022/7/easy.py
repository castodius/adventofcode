import sys

LIMIT = 10**5
total = 0

class Node():
  def __init__(self, name):
    self.name = name
    self.parent = None
    self.children = []
    self.files = []

  def add_child(self, child):
    child.set_parent(self)
    self.children.append(child)

  def set_parent(self, parent):
    self.parent = parent

  def add_file(self, name, size):
    self.files.append((name, size))

  def sum(self):
    total_size = 0
    for file in self.files:
      total_size += file[1]

    for child in self.children:
      total_size += child.sum()

    global total
    if total_size <= LIMIT:
      total += total_size

    return total_size
    

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

top.sum()
print(total)
