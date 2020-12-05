import sys

def solve(line):
  low = 0
  high = 127
  for char in line[:-3]:
    if char == 'F':
      high = low + (high-low) / 2
    else:
      low = low + (high-low) / 2 + 1

  row = low

  low = 0
  high = 7
  for char in line[-3:]:
    if char == 'L':
      high = low + (high-low) / 2
    else:
      low = low + (high-low) / 2 + 1

  seat = low
  return row, seat

rows = [[] for _ in range(128)]
for line in sys.stdin:
  line = line.strip()
  row, seat = solve(line)
  rows[row].append(seat)

for index, row in enumerate(rows):
  if len(row) == 7:
    for seat in range(8):
      if not seat in row:
        print index*8+seat
        break