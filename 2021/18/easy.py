import sys
import re
import json

LEFT = 0
RIGHT = 1

def explode(a, level):
  left, right = a

  if level == 4:
    print left, right
    return (True, 'EXPLODE'+str(left)+','+str(right))
  
  if type(left) is list:
    changed, value = explode(left, level+1)
    if changed:
      a[LEFT] = value
      return (True, a)

  if type(right) is list:
    changed, value = explode(right, level+1)
    if changed:
      a[RIGHT] = value
      return (True, a)
    
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

def process_explode(s):
  s = json.dumps(s)
  pattern = '"EXPLODE\d,\d"'
  values = re.findall(pattern, s)[0]
  left_value, right_value = map(int, values[8:-1].split(','))
  left, right = re.split(pattern, s)

  left_values = re.findall('\d', left)
  if len(left_values) != 0:
    right_most = left_values[-1]
    left_value += int(right_most)
    left_value = str(left_value)
    data = left.split(right_most)
    left = right_most.join(data[:-1])+left_value+data[-1]

  right_values = re.findall('\d', right)
  if len(right_values) != 0:
    left_most = right_values[0]
    right_value += int(left_most)
    right_value = str(right_value)
    data = right.split(left_most)
    right = data[0] + right_value + left_most.join(data[1:])

  return eval(left+'0'+right)

def add(a, b):
  current = [a,b]

  while True:
    changed, current = explode(current, 0)
    if changed:
      current = process_explode(current)
      return
      
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
_, ans = explode([7,[6,[5,[4,[3,2]]]]], 0)
print process_explode(ans)
