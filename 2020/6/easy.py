import sys

ans = set()
count = 0
total = 0
for line in sys.stdin:
  line = line.strip()
  if line == '':
    count += len(ans)
    ans = set()
    total = 0
    continue

  for char in line:
    ans.add(char)

count += len(ans)
print count