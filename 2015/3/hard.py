seen = set()
seen.add((0,0))

line = raw_input().strip()

def solve(chars):
  x,y = 0,0
  count = 0
  for char in chars:
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

  return count

print 1+solve(line[::2])+solve(line[1::2])