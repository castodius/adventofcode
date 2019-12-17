import sys

m = {}

def solve(line, c):
  min_value = 10**6
  x,y = 0,0
  for val in line.split(','):
    dx, dy = 0,0
    dir = val[0]
    if dir == 'R':
      dx = 1
    elif dir == 'U':
      dy = 1
    elif dir == 'L':
      dx = -1
    elif dir == 'D':
      dy = -1
    
    steps = int(val[1:])
    for _ in range(steps):
      x += dx
      y += dy
      tup = (x,y)
      if tup in m and m[tup] != c:
        min_value = min(min_value, abs(x)+abs(y))
      
      m[tup] = c
  
  return min_value


lines = [line for line in sys.stdin]
solve(lines[0], 'a')
print solve(lines[1], 'b')