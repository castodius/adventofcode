import sys

rows = []
for line in sys.stdin:
  rows.append(line.strip())

row_length = len(rows[0])
count = 0
index = 3
for row in rows[1:]:
  if row[index] == '#':
    count += 1
  index+=3
  index%=row_length

print count