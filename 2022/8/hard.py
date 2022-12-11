import sys

forest = []
for line in sys.stdin:
  line = line.strip()
  trees = [int(tree) for tree in line]
  forest.append(trees)

best = 0
for y, row in enumerate(forest[1:-1],1):
  for x, tree in enumerate(row[1:-1],1):
    scenic_score = 1
    max_allowed = tree

    tmp_x = x-1
    while tmp_x > 0:
      tree = forest[y][tmp_x]
      if tree >= max_allowed:
        break

      tmp_x -= 1

    scenic_score *= x-tmp_x

    tmp_x = x + 1
    while tmp_x < len(row) - 1:
      tree = forest[y][tmp_x]
      if tree >= max_allowed:
        break

      tmp_x += 1

    scenic_score *= tmp_x-x


    tmp_y = y-1
    while tmp_y > 0:
      tree = forest[tmp_y][x]
      if tree >= max_allowed:
        break

      tmp_y -= 1

    scenic_score *= y-tmp_y

    tmp_y = y+1
    while tmp_y < len(forest) - 1:
      tree = forest[tmp_y][x]
      if tree >= max_allowed:
        break

      tmp_y += 1

    scenic_score *= tmp_y-y

    best = max(best, scenic_score)

print(best)
