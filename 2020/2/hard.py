import sys

def solve(line):
  counts, char, password = line.strip().split(' ')
  low, high = map(int, counts.split('-'))
  char = char[0]
  low_true = password[low-1] == char
  high_true = password[high-1] == char

  return (low_true and not high_true) or (not low_true and high_true)

count = 0
for line in sys.stdin:
  if solve(line):
    count += 1

print count