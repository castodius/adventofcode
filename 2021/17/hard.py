import sys

MISS = -10**5

_, data = sys.stdin.readline().split(': ')
xs, ys = data.split(', ')
xs = map(int, xs[2:].split('..'))
ys = map(int, ys[2:].split('..'))
min_x, max_x = xs
min_y, max_y = ys

def calc_y(y):
  steps = 0
  hits = []
  current = 0
  while True:
    steps += 1
    current += y
    if min_y <= current <= max_y:
      hits.append(steps)
    if current < min_y:
      return hits
    y -= 1

def calc_x(x, steps):
  current = 0
  min_step, max_step = steps[0], steps[-1]
  for step in range(1, max_step+1):
    current += x
    if x != 0:
      x += 1 if x < 0 else -1
    if step  < min_step:
      continue
    if  min_x <= current <= max_x:
      return 1
  return 0

def solve():
  total = 0
  for y in range(-1000, 1000):
    steps = calc_y(y)
    if len(steps) == 0:
      continue

    for x in range(-1000, 1000):
      new_hits = calc_x(x, steps)
      if new_hits > 0:
        total += new_hits
  return total

print solve()
