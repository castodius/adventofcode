import sys

vis = set()
vis.add((0,0))
head_x, head_y = 0, 0
tail_x, tail_y = 0, 0

def touching():
  return abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1

def move(dir):
  global tail_y, tail_x
  if dir == 'R' or dir == 'L':
    if head_y != tail_y:
      tail_y = head_y

    if dir == 'R':
      tail_x += 1
    else:
      tail_x -= 1

  else:
    if head_x != tail_x:
      tail_x = head_x

    if dir == 'U':
      tail_y += 1
    else:
      tail_y -= 1
  
  vis.add((tail_x, tail_y))

for line in sys.stdin:
  dir, steps = line.strip().split(' ')
  steps = int(steps)

  for step in range(steps):
    if dir == 'R':
      head_x += 1
    elif dir == 'L':
      head_x -= 1
    elif dir == 'U':
      head_y += 1
    else:
      head_y -= 1

    if touching():
      continue

    move(dir)

print(len(vis))
