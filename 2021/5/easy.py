import sys
from collections import defaultdict

visits = defaultdict(lambda:0)

def parseCoords(s):
  return map(int, s.split(','))

def solve():
  lines = [line.strip() for line in sys.stdin]
  for line in lines:
    v1, v2 = line.split(' -> ')
    x1, y1 = parseCoords(v1)
    x2, y2 = parseCoords(v2)

    [x1, y1], [x2, y2] = sorted([[x1, y1], [x2, y2]])

    if x1 == x2:
      for y in range(y1, y2+1):
        visits[(x1, y)] += 1
    elif y1 == y2:
      for x in range(x1, x2+1):
        visits[(x, y1)] += 1

  return sum([1 for value in visits.values() if value > 1])
print solve()
