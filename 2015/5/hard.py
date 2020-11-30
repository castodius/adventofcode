import sys

NOT_SEEN = -1

def has_pair(line):
  seen = {}
  for index in range(len(line)-1):
    pair = line[index:index+2]
    prev = seen.get(pair, NOT_SEEN)
    if prev != NOT_SEEN:
      if index-prev >=2:
        return True
    else:
      seen[pair] = index

  return False

def has_repetition(line):
  for index, letter in enumerate(line[:-2]):
    if letter == line[index+2]:
      return True

  return False

def solve(line):
  return has_pair(line) and has_repetition(line)

count = 0
for line in sys.stdin:
  if solve(line.strip()):
    count += 1

print count
