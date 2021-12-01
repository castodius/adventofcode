import sys

def solve():
  measurements = [int(line) for line in sys.stdin]

  prev = 0
  increases = 0
  for index, _ in enumerate(measurements[1:-2]):
    curr = sum(measurements[index:index+3])
    if curr > prev:
      increases += 1
    prev = curr
  return increases

print solve()
