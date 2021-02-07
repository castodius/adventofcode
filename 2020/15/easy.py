values = map(int, raw_input().strip().split(','))

indexes = {}
for index, value in enumerate(values):
  indexes[value] = [index]

index = len(values)
target = 2020
curr = 0
while index < target - 1:
  if not curr in indexes:
    indexes[curr] = []
    indexes[curr].append(index)
    curr = 0
  else:
    tmp = curr
    curr = index - indexes[curr][-1]
    indexes[tmp].append(index)

  index += 1

print curr
