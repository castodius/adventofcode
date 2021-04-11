import sys

ACTIVE = '#'
INACTIVE = '.'
CYCLES = 6

class Matrix:
  def __init__(self, side):
    self.CENTER=side/2
    self.SIDE=side
    self.matrix = [ 
      [ 
        [INACTIVE for _ in range(self.SIDE)]
          for _ in range(self.SIDE)
        ] for _ in range(self.SIDE)
      ]

  def get_center(self):
    return self.SIDE/2

  def get_side(self):
    return self.SIDE

  def get_active_neighbours(self, x, y, z):
    deltas = [-1, 0, 1]
    active = 0
    for xd in deltas:
      for yd in deltas:
        for zd in deltas:
          if xd == 0 and yd == 0 and zd == 0:
            continue
          active += 1 if self.matrix[x+xd][y+yd][z+zd] == ACTIVE else 0
    return active

  def get_active_count(self):
    count = 0
    for z in self.matrix:
      for y in z:
        for x in y:
          count += 1 if x == ACTIVE else 0

    return count

def init():
  rows = [row.strip() for row in sys.stdin]
  n = len(rows[0])
  matrix = Matrix((n/2+2+CYCLES)*2)
  SHIFT = matrix.get_center() - n/2
  for index, row in enumerate(rows):
    matrix.matrix[matrix.get_center()][SHIFT+index][SHIFT:SHIFT+n] = [char for char in row]

  return matrix

def run_cycle(matrix):
  side = matrix.get_side()
  new_matrix = Matrix(matrix.get_side())
  for x in range(1, side-1):
    for y in range(1, side-1):
      for z in range(1, side-1):
        count = matrix.get_active_neighbours(x, y, z)
        if matrix.matrix[x][y][z] == ACTIVE:
          if 2 <= count <= 3:
            new_matrix.matrix[x][y][z] = ACTIVE
        else:
          if count == 3:
            new_matrix.matrix[x][y][z] = ACTIVE

  return new_matrix

matrix = init()
for i in range(CYCLES):
  matrix = run_cycle(matrix)

print matrix.get_active_count()
