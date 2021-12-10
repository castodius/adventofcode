import sys

ILLEGAL = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137
}

CLOSERS = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4
}

PAIR = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>'
}

OPENERS = set(PAIR.keys())

def calc(chars):
  chars = chars[::-1]
  score = 0
  for char in chars:
    score *= 5
    score += CLOSERS[char]
  return score

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
        return 0
      index -= 1

  return calc(stack[:index+1])

def solve():
  lines = [line.strip() for line in sys.stdin]
  scores = [is_corrupt(line) for line in lines]
  scores = [score for score in scores if score != 0]
  scores.sort()
  return scores[len(scores)/ 2]

print solve()
