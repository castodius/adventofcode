import sys

FREE = 'L'
OCCUPIED = '#'
FLOOR = '.'

seats = []
for line in sys.stdin:
  seats.append(line.strip())

ROWS = len(seats)
COLUMNS = len(seats[0])

def get_surroundings(x, y):
  free, occupied, floor = 0, 0, 0
  for dy in range(y-1, y+2):
    for dx in range(x-1, x+2):
      if dx == x and dy == y:
        continue
      if dx < 0 or dx >= COLUMNS:
        continue
      if dy < 0 or dy >= ROWS:
        continue
      seat = seats[dy][dx]
      if seat == FREE:
        free += 1
      elif seat == OCCUPIED:
        occupied += 1
      else:
        floor += 1
  
  return {
    'free': free,
    'occupied': occupied,
    'floor': floor
  }

def update(seats):
  new_state = []
  change = False
  for cindex, row in enumerate(seats):
    new_state.append('')
    for rindex, seat in enumerate(row):
      if seat == FLOOR:
        new_state[cindex]+=FLOOR
        continue
      surroundings = get_surroundings(rindex, cindex)
      if seat == FREE:
        if surroundings['occupied'] == 0:
          new_state[cindex] += OCCUPIED
          change = True
          continue
        else:
          new_state[cindex] += FREE
      if seat == OCCUPIED:
        if surroundings['occupied'] >= 4:
          new_state[cindex] += FREE
          change = True
          continue
        else:
          new_state[cindex] += OCCUPIED

  return change, new_state

def get_count():
  return sum([row.count(OCCUPIED) for row in seats])

changed = True
while changed:
  changed, updated = update(seats)
  seats = updated

print get_count()
