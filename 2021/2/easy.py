import sys

def solve():
  commands = [line.strip() for line in sys.stdin]
  x = y = 0
  for command in commands:
    dir, value = command.split(' ')
    value = int(value)
    if dir == 'forward':
      x += value
    elif dir == 'down':
      y += value
    else:
      y -= value

  return x*y

print solve()