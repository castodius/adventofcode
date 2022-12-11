import sys

cycle = 1
total = 0
register = 1

def check_cycle():
  global total
  if cycle in [20, 60, 100, 140, 180, 220]:
    total += register*cycle

for operation in sys.stdin:
  operation = operation.strip()
  check_cycle()
  
  if operation == 'noop':
    cycle += 1
    continue

  _, value = operation.split(' ')
  value = int(value)
  cycle += 1
  check_cycle()
  cycle += 1
  register += value

print(total)