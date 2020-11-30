import sys

def solve(line):
  l,w,h = map(int, line.strip().split('x'))

  areas = [l*w, l*h, w*h]

  return 2*sum(areas)+min(areas)

total = 0
for line in sys.stdin:
  total += solve(line)

print total