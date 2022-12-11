import sys

WIDTH = 40
HEIGHT = 6
screen = [['.']*WIDTH for _ in range(HEIGHT)]

def get_row_and_column(cycle):
  row = cycle // WIDTH
  column = cycle % WIDTH
  return row, column

def in_range(register, column):
  return register - 1 <= column <= register + 1

def update_screen(register, column, row):
  if in_range(register, column):
    screen[row][column] = '#'

cycle = 0
register = 1
for operation in sys.stdin:
  operation = operation.strip()
  row, column = get_row_and_column(cycle)

  if operation == 'noop':
    update_screen(register, column, row)
    cycle += 1
    continue

  _, value = operation.split(' ')
  value = int(value)
  update_screen(register, column, row)
  cycle += 1
  row, column = get_row_and_column(cycle)
  update_screen(register, column, row)
  cycle += 1
  register += value

for row in screen:
  print(''.join(row))