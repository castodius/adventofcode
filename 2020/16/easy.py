import sys

class NumberContainer: # bad name is bad?
  def __init__(self):
    self.valid = set()

  def add(self, string_range):
    a, b = map(int, string_range.split('-'))
    for i in range(a, b+1):
      self.valid.add(i)

  def has_value(self, value):
    return value in self.valid

def update_ranges(container, row):
  row = row.split(': ')[1]
  range1, range2 = row.split(' or ')
  container.add(range1)
  container.add(range2)

def get_count(container, row):
  count = 0
  values = map(int, row.split(','))
  for value in values:
    if not container.has_value(value):
      count += value
  return count

container = NumberContainer()
rows = [row.strip() for row in sys.stdin]
count = 0
round = 0
for row in rows:
  if row == '' or 'nearby' in row:
    round += 1
    continue
  if round == 0:
    update_ranges(container, row)
  elif round == 1:
    pass
  else:
    count += get_count(container, row)

print count
