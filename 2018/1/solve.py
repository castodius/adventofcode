import sys

total = 0
for line in sys.stdin:
  value = int(line[1:])
  if '+' in line:
    total+=value
  else:
    total-=value

print total
    