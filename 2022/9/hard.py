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

  if abs(head_x - tail_x) > 1:
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
   #print(knots)


print(knots)
print(len(vis))
#print(vis)