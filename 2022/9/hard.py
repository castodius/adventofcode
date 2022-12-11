import sys

vis = set()
vis.add((0,0))
knots = [[0,0]for _ in range(10)]

def touching(point_one, point_two):
  return abs(point_one[0] - point_two[0]) <= 1 and abs(point_one[1] - point_two[1]) <= 1

def move(head_index, tail_index):
  head, tail = knots[head_index:tail_index+1]
  head_x, head_y = head
  tail_x, tail_y = tail

  if abs(head_x - tail_x) > 1 and abs(head_y - tail_y) > 1:
    if head_x > tail_x:
      knots[tail_index][0] += 1
    else:
      knots[tail_index][0] -= 1

    if head_y > tail_y:
      knots[tail_index][1] += 1
    else:
      knots[tail_index][1] -= 1

  elif abs(head_x - tail_x) > 1:
    knots[tail_index][1] = head_y

    if head_x > tail_x:
      knots[tail_index][0] += 1
    else:
      knots[tail_index][0] -= 1
  else:
    knots[tail_index][0] = head_x

    if head_y > tail_y:
      knots[tail_index][1] += 1
    else:
      knots[tail_index][1] -= 1

def update_knots():
  for index, point in enumerate(knots[0:-1]):
    if touching(point, knots[index+1]):
      break
    move(index, index+1)

SCREEN_SIZE = 12
def render():
  screen = [['.']*SCREEN_SIZE for _ in range(SCREEN_SIZE)]
  screen[SCREEN_SIZE//2][SCREEN_SIZE//2] = 's'
  for index, knot in enumerate(knots[::-1]):
    x, y = knot
    x += SCREEN_SIZE//2
    y += SCREEN_SIZE//2
    screen[y][x] = 'H' if index == 9 else str(9-index)

  for row in screen[::-1]:
    print(''.join(row))
  print()


lines = [line for line in sys.stdin]
for line in lines:
  dir, steps = line.strip().split(' ')
  steps = int(steps)

  for step in range(steps):
    if dir == 'R':
      knots[0][0] += 1
    elif dir == 'L':
      knots[0][0] -= 1
    elif dir == 'U':
      knots[0][1] += 1
    else:
      knots[0][1] -= 1

    update_knots()
    vis.add((knots[-1][0], knots[-1][1]))
    #render()

print(len(vis))