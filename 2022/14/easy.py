import sys

WIDTH = 600
HEIGHT = 600

VOID = '.'
ROCK = '#'
SAND = 'o'

cave = [[VOID]*WIDTH for _ in range(HEIGHT)]

def unpack_point(point):
  return map(int, point.split(','))

for line in sys.stdin:
  points = line.strip().split(' -> ')
  points = list(map(unpack_point, points))
  x,y = points[0]
  cave[y][x] = ROCK
  for point in points[1:]:
    dst_x, dst_y = point
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

def solve():
  sand_units = 0
  while True:
    y, x = 0, 500
    while True:
      if y == len(cave) - 1:
        return sand_units

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

#cave[0][50] = '+'
""" for row in cave:
  print(''.join(row)) """
