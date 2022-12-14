import sys

WIDTH = 1000
HEIGHT = 500

VOID = '.'
ROCK = '#'
SAND = 'o'

cave = [[VOID]*WIDTH for _ in range(HEIGHT)]

def unpack_point(point):
  return map(int, point.split(','))

max_y = 0

for line in sys.stdin:
  points = line.strip().split(' -> ')
  points = list(map(unpack_point, points))
  x, y = points[0]
  max_y = max(y, max_y)

  cave[y][x] = ROCK
  for point in points[1:]:
    dst_x, dst_y = point
    max_y = max(dst_y, max_y)
    if x == dst_x:
      while y != dst_y:
        if dst_y < y:
          y -= 1
        else:
          y += 1

        cave[y][x] = ROCK
    else:
      while x != dst_x:
        if dst_x < x:
          x -= 1
        else:
          x += 1
        
        cave[y][x] = ROCK

max_y += 2

cave[max_y] = [ROCK] * WIDTH

def solve():
  sand_units = 0
  while True:
    if cave[0][500] == SAND:
      return sand_units
    y, x = 0, 500
    while True:
      if cave[y+1][x] == VOID:
        y += 1
        continue

      if cave[y+1][x-1] == VOID:
        x -= 1
        continue

      if cave[y+1][x+1] == VOID:
        x += 1
        continue

      cave[y][x] = SAND
      sand_units += 1
      break

print(solve())
