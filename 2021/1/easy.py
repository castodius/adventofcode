import sys

def solve():
  measurements = []
  for line in sys.stdin:
    measurements.append(int(line))

  prev = measurements[0]
  increases = 0
  for measurement in measurements[1:]:
    if measurement > prev:
      increases += 1
    prev = measurement
  return increases

print solve()