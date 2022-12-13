import sys
import json
from functools import cmp_to_key

LEFT = 1
EQUAL = 0
RIGHT = -1

def comparator(left, right):
  left_type = type(left)
  right_type = type(right)

  if left_type == list and right_type == list:
    for index, left_item in enumerate(left):
      if index == len(right):
        return LEFT

      res = comparator(left_item, right[index])
      if res != EQUAL:
        return res
    else:
      if len(left) < len(right):
        return RIGHT
      return EQUAL

  if left_type == list:
    return comparator(left, [right])

  if right_type == list:
    return comparator([left], right)

  if left == right:
    return EQUAL

  return RIGHT if left < right else LEFT
  
total = 0

data = sys.stdin.read()
data = [row for row in data.split('\n\n')]
groupings = [[2], [6]]
for row in data:
  a,b = map(json.loads, row.split('\n'))
  groupings.append(a)
  groupings.append(b)

groupings.sort(key=cmp_to_key(comparator))
result = 1
for index, grouping in enumerate(groupings, 1):
  if grouping in [[2],[6]]:
    result *= index
print(result)