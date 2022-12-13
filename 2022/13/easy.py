import sys
import json

FAIL = 0
EQUAL = 1
SUCCESS = 2

def iter(left, right):
  left_type = type(left)
  right_type = type(right)

  if left_type == list and right_type == list:
    for index, left_item in enumerate(left):
      if index == len(right):
        return FAIL

      res = iter(left_item, right[index])
      if res != EQUAL:
        return res
    else:
      if len(left) < len(right):
        return SUCCESS
      return EQUAL

  if left_type == list:
    return iter(left, [right])

  if right_type == list:
    return iter([left], right)

  if left == right:
    return EQUAL

  return SUCCESS if left < right else FAIL

def solve(grouping):
  left,right = grouping.split('\n')
  left = json.loads(left)
  right = json.loads(right)
  return iter(left, right)
  
total = 0

data = sys.stdin.read()

groupings = [grouping for grouping in data.split('\n\n')]
for index, grouping in enumerate(groupings, 1):
  total += index if solve(grouping) == SUCCESS else 0

print(total)
