import sys

adapters = [int(line) for line in sys.stdin]
adapters.sort()

diff1 = 0
diff3 = 1
prev = 0
for adapter in adapters:
  diff = adapter - prev
  if diff == 1:
    diff1 += 1
  elif diff == 3:
    diff3 += 1
  prev = adapter

print diff1*diff3