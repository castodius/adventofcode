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
easting = 10
northing = 1
for action, value in instructions:
  if action == 'F':
    x += easting*value
    y += northing*value
    continue

  if action in compass_directions:
    dx = compass_directions[action]['dx']
    dy = compass_directions[action]['dy']
    northing += dy*value
    easting += dx*value
    continue

  if action == 'L':
    value = 360 - value

  while value > 0:
    easting, northing = northing, -easting
    value -= 90

print abs(x)+abs(y)