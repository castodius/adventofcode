import sys

def solve(rows, right, down):
  row_length = len(rows[0])
  count = 0
  index = right
  for row in rows[down::down]:
    if row[index] == '#':
      count += 1
    index+=right
    index%=row_length

  return count

rows = []
for line in sys.stdin:
  rows.append(line.strip())

combos = [(1,1), (3,1), (5,1), (7,1), (1,2)]

count = 1
for right, down in combos:
  count *= solve(rows, right, down)

print count