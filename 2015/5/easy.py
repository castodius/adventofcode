import sys

def vowels(line):
  return sum([line.count(vowel) for vowel in 'aeiou']) >= 3

def pair(line):
  for index in range(len(line)-1):
    if line[index] == line[index+1]:
      return True
  return False

pairs = ['ab', 'cd', 'pq', 'xy']
def bad_pairs(line):
  for pair in pairs:
    if line.count(pair) > 0:
      return True
  return False

def solve(line):
  return vowels(line) and pair(line) and not bad_pairs(line)

count = 0
for line in sys.stdin:
  if solve(line.strip()):
    count += 1

print count