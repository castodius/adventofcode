import sys

def solve(line):
  l,w,h = map(int, line.strip().split('x'))

  lens = [l,w,h]
  lens.sort()

  return l*w*h + 2*(lens[0]+lens[1])

total = 0
for line in sys.stdin:
  total += solve(line)

print total