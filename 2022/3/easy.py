import sys
from string import ascii_lowercase, ascii_uppercase

lines = [line.strip() for line in sys.stdin]

total = 0
for line in lines:
  length = len(line)//2
  first_half = set(line[0:length])
  second_half = set(line[length:])
  char = list(first_half & second_half)[0]

  if char in ascii_lowercase:
    total += ascii_lowercase.index(char) + 1
  else:
    total += ascii_uppercase.index(char) + 27

print(total)
