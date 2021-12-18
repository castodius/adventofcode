import sys

MISS = -10**5

_, ys = sys.stdin.readline().split('y=')
ys = map(int, ys.split('..'))
min_y, max_y = ys

def calc(y):
  high = 0
  current = 0
  while True:
    current += y
    if min_y <= current <= max_y:
      return high
    if current < min_y:
      return MISS
    high = max(high, current)
    y -= 1

def solve():
  best = MISS
  for y in range(-1000, 1000):
    value = calc(y)
    if value == MISS:
      continue
    best = max(best, value)
  return best

print solve()