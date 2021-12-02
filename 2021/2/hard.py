import sys

def solve():
  commands = [line.strip() for line in sys.stdin]
  aim = x = y = 0
  for command in commands:
    dir, value = command.split(' ')
    value = int(value)
    if dir == 'forward':
      x += value
      y += value * aim
    elif dir == 'down':
      aim += value
    else:
      aim -= value
  return x*y

print solve()