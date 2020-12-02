import sys

def solve(line):
  counts, char, password = line.strip().split(' ')
  low, high = map(int, counts.split('-'))
  char = char[0]
  return low <= password.count(char) <= high

count = 0
for line in sys.stdin:
  if solve(line):
    count += 1

print count