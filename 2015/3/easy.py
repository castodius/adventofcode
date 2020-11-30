seen = set()
seen.add((0,0))
count = 1

x,y = 0,0
line = raw_input().strip()

for char in line:
  if char == '>':
    x += 1
  elif char == '<':
    x -= 1
  elif char == '^':
    y += 1
  else:
    y -= 1

  if not (x,y) in seen:
    count += 1

  seen.add((x,y))

print count