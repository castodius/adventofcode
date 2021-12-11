import sys

ROUNDS = 100
TRIGGER = 10
MAX_Y = 10
MAX_X = 10
deltas = [[1,0], [1,1], [0,1], [-1,1], [-1,0], [-1,-1], [0,-1], [1, -1]]

def trim(n):
  if n >= TRIGGER:
    return 0
  return n

def solve():
  animals = [[int(char) for char in line.strip()] for line in sys.stdin]

  total = 0
  for round in range(ROUNDS):
    animals = [[animal + 1 for animal in line] for line in animals]
    flashed = [[False]*10 for _ in range(10)]

    new_flash = True
    flashes = 0
    while new_flash:
      new_flash = False
      for y in range(MAX_Y):
        for x in range(MAX_X):
          if flashed[y][x]:
            continue
          if animals[y][x] >= TRIGGER:
            flashes += 1
            flashed[y][x] = True
            new_flash = True
          else:
            continue

          for dx, dy in deltas:
            new_y = y+dy
            new_x = x+dx
            if new_y < 0 or new_y == MAX_Y or new_x < 0 or new_x == MAX_X:
              continue
            animals[new_y][new_x] += 1

    animals = [[trim(animal) for animal in line] for line in animals]
    total += flashes
  return total


print solve()
