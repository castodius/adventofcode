import sys

def solve():
  values = []
  for line in sys.stdin:
    tmp = [line.split('| ')[1].strip().split(' ')]
    values = values + tmp

  total = 0
  for line in values:
    for value in line:
      if len(value) == 5 or len(value) == 6:
        continue
      total += 1

  return total
print solve()
