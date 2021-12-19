import sys

LEFT = 0
RIGHT = 1

def explode(a, level):
  if level == 4:
    pass
  return (False, a)

def split(a):
  left, right = a
  if type(left) is int:
    if left >= 10:
      a[LEFT] = [left/2, (left+1)/2]
      return (True, a)
  else:
    changed, value = split(left)
    if changed:
      a[LEFT] = value
      return (True, a)

  if type(right) is int:
    if right >= 10:
      a[1] = [right/2, (right+1)/2]
      return (True, a)
  else:
    changed, value = split(right)
    if changed:
      a[RIGHT] = value
      return (True, a)
  
  return (False, a)

def add(a, b):
  current = [a,b]

  while True:
    changed, current = explode(current, 0)
    if changed:
      continue
    
    changed, current = split(current)
    if changed:
      continue

    return current

def solve():
  numbers = [eval(line) for line in sys.stdin]

  current = numbers[0]
  for number in numbers[1:]:
    current = add(current, number)

#print solve()
_, ans = split([[[[0,7],4],[15,[0,13]]],[1,1]])
print ans
_, ans = split(ans)
print ans
