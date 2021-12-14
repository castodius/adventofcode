import sys
from collections import defaultdict

ITER = 40

def solve():
  lines = [line.strip() for line in sys.stdin]
  pairs = defaultdict(lambda:0)
  letters = set()
  for index in range(len(lines[0])-1):
    pair = lines[0][index:index+2]
    pairs[pair] += 1

  transitions = {}
  for line in lines[2:]:
    src, dst = line.split(' -> ')
    transitions[src] = dst
    for letter in src:
      letters.add(letter)
    for letter in dst:
      letters.add(letter)

  for _ in range(ITER):
    new_pairs = defaultdict(lambda:0)
    for key, value in pairs.items():
      insert = transitions[key]
      key_one = key[0]+insert
      key_two = insert+key[1]
      new_pairs[key_one] += value
      new_pairs[key_two] += value
    pairs = new_pairs

  counts = []
  for letter in letters:
    start = 0
    end = 0
    middle_key = letter*2
    middle = pairs[middle_key]
    for key, value in pairs.items():
      if key == middle_key:
        continue
      if key[1] == letter:
        start += value
      elif key[0] == letter:
        end += value

    counts.append((middle+max(start, end),letter))

  counts.sort()
  return counts[-1][0] - counts[0][0]

print solve()
