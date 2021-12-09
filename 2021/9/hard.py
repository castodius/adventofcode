import sys

FORBIDDEN = 9

lines = [[int(value) for value in line.strip()] for line in sys.stdin]
y_len = len(lines)
x_len = len(lines[0])
visited = [[False]*x_len for _ in range(y_len)]

def search(y, x):
  if visited[y][x]:
    return 0
  value = lines[y][x]
  if value == FORBIDDEN:
    return 0

  total = 0
  visited[y][x] = True
  for dy, dx in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
    tmp_y = y+dy
    tmp_x = x+dx
    if tmp_y < 0 or tmp_y == y_len or tmp_x < 0 or tmp_x == x_len:
      continue
    total += search(tmp_y, tmp_x)
  return total + 1

def solve():
  values = []
  for y in range(y_len):
    for x in range(x_len):
      value = search(y, x)
      values.append(value)

  total = 1
  values.sort()
  for value in values[-3:]:
    total *= value
  return total
 
print solve()
