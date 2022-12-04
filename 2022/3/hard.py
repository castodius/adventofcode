import sys
from string import ascii_lowercase, ascii_uppercase

lines = [line.strip() for line in sys.stdin]

total = 0
for index in range(0, len(lines),3):
  char = list(set(lines[index]) & set(lines[index+1]) & set(lines[index+2]))[0]
  if char in ascii_lowercase:
    total += ascii_lowercase.index(char) + 1
  else:
    total += ascii_uppercase.index(char) + 27

print(total)
