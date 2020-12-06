import sys

ans = set()
count = 0
total = 0
first = True
for line in sys.stdin:
  line = line.strip()
  if line == '':
    count += len(ans)
    ans = set()
    total = 0
    first = True
    continue

  if first:
    for char in line:
      ans.add(char)
    first = False
  else:
    ans = ans.intersection(set([char for char in line]))

count += len(ans)
print count
