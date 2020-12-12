import sys

instructions = []
for line in sys.stdin:
  line = line.strip()
  instructions.append((line[0], int(line[1:])))

compass_directions = {
  'N': {
    'dx': 0,
    'dy': 1
  },
  'W': {
    'dx': -1,
    'dy': 0
  },
  'S': {
    'dx': 0,
    'dy': -1
  },
  'E': {
    'dx': 1,
    'dy': 0
  }
}
dirs = ['N', 'E', 'S', 'W']

x, y = 0, 0
direction = 'E'
for action, value in instructions:
  if action == 'F':
    action = direction

  if action in compass_directions:
    dx = compass_directions[action]['dx']
    dy = compass_directions[action]['dy']
    x += dx*value
    y += dy*value
  else:
    modifier = 1
    if action == 'L':
      modifier = -1

    index = dirs.index(direction)
    while value > 0:
      value -= 90
      index += modifier

    index %= 4
    direction = dirs[index]

print abs(x)+abs(y)