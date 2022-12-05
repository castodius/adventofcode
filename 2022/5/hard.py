import sys

rows = []
for line in sys.stdin:
  if len(line.strip()) == 0:
    break
  rows.append(line)

number_columns = len(rows[0])//4
columns = [[] for _ in range(number_columns)]

for row in rows[:-1]:
  for column in range(0, number_columns, 1):
    element = row[column*4+1]
    if element == ' ':
      continue
    columns[column].append(element)

instructions = []
for line in sys.stdin:
  _, count, _, src, _, dst = line.split(' ')
  count, src, dst = map(int, [count, src, dst])
  src -= 1
  dst -= 1

  crates = columns[src][:count]
  columns[src] = columns[src][count:]
  columns[dst] = crates + columns[dst]

ans = ''.join([column[0] for column in columns])
print(ans)