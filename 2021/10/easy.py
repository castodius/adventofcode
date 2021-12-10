import sys

ILLEGAL = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137
}

PAIR = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>'
}

OPENERS = set(PAIR.keys())

def is_corrupt(line):
  stack = ['']*1000
  index = -1
  for char in line:
    if char in OPENERS:
      index += 1
      stack[index] = PAIR[char]
    else:
      if index == -1:
        return ILLEGAL[char]
      top = stack[index]
      if top != char:
        return ILLEGAL[char]
      index -= 1
  return 0

def solve():
  lines = [line.strip() for line in sys.stdin]
  return sum([is_corrupt(line) for line in lines])

print solve()
