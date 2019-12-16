import sys
import math

def solve(n):
  return int(math.floor(n/3)-2)

print sum([solve(int(line)) for line in sys.stdin])
    