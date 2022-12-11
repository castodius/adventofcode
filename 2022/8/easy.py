import sys

forest = []
for line in sys.stdin:
  line = line.strip()
  trees = [(int(tree), False) for tree in line]
  forest.append(trees)

visible = 0

def scan(graph):
  for y, row in enumerate(graph):
    curr, seen = row[0]
    global visible
    if not seen:
      visible += 1
    row[0] = (curr, True)

    for x, item in enumerate(row):
      tree, seen = item
      if curr < tree:
        if not seen:
          graph[y][x] = (tree, True)
          visible += 1
        curr = tree

# scan right
scan(forest)
forest = [row[::-1] for row in forest]
# scan left
scan(forest)
forest = [list(row) for row in zip(*forest)]
# scan down
scan(forest)
forest = [row[::-1] for row in forest]
# scan up
scan(forest)

print(visible)
