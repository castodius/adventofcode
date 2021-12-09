import sys

def solve():
  lines = [[int(value) for value in line.strip()] for line in sys.stdin]
  values = []
  y_len = len(lines)
  x_len = len(lines[0])
  for y in range(y_len):
    for x, value in enumerate(lines[y]):
      if y > 0 and lines[y-1][x] <= value:
        continue
      if y < y_len - 1 and lines[y+1][x] <= value:
        continue
      if x > 0 and lines[y][x-1] <= value:
        continue
      if x < x_len - 1 and lines[y][x+1] <= value:
        continue
      values.append(value)
  return len(values)+sum(values)
 
print solve()
