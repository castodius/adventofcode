import sys

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
def solve(keys):
  for key in required:
    if not key in keys:
      return False
  return True

keys = []
count = 0
for line in sys.stdin:
  line = line.strip()
  if line == '':
    if solve(keys):
      count += 1
    keys = []

  data = line.split(' ')
  keys.extend(map(lambda x: x.split(':')[0], data))

if solve(keys):
  count += 1

print count