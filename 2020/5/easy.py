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

  return row*8 + low

highest = 0
for line in sys.stdin:
  line = line.strip()
  highest = max(highest, solve(line))

print highest