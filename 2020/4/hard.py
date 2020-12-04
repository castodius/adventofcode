import sys
import re

def validateNumber(value, low, high):
  if not value.isdigit():
    return False
  value = int(value)
  if value < low or value > high:
    return False

  return True

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
def solve(data):
  seen = set()
  for item in data:
    key, value = item.split(':')
    seen.add(key)
    if key == 'cid':
      continue

    if key == 'byr':
      good = validateNumber(value, 1920, 2002)
      if not good:
        return False

    if key == 'iyr':
      good = validateNumber(value, 2010, 2020)
      if not good:
        return False

    if key == 'eyr':
      good = validateNumber(value, 2020, 2030)
      if not good:
        return False

    if key == 'hgt':
      if 'cm' in value:
        value = value[:-2]
        good = validateNumber(value, 150, 193)
        if not good:
          return False
      else:
        value = value[:-2]
        good = validateNumber(value, 59, 76)
        if not good:
          return False

    if key == 'hcl':
      if len(re.findall('^#[a-z0-9]{6}$', value)) != 1:
        return False

    if key == 'ecl':
      if not value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if key == 'pid':
      if len(re.findall('^[0-9]{9}$', value)) != 1:
        return False

  for key in required:
    if not key in seen:
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
    continue

  data = line.split(' ')
  keys.extend(data)

if solve(keys):
  count += 1

print count