import sys

def count_values(rows, position):
    values = [row[position] for row in rows]
    ones = values.count('1')
    zeroes = values.count('0')
    return [zeroes, ones]


def get_most_common(rows, position):
    zeroes, ones = count_values(rows, position)
    most_common = '1' if ones >= zeroes else '0'
    return most_common

def get_least_common(rows, position):
    zeroes, ones = count_values(rows, position)
    if zeroes == 0:
      return '1'
    if ones == 0:
      return '0'
    least_common = '0' if zeroes <= ones else '1'
    return least_common

def get_oxygen(rows):
  rows = rows[:]
  value = ''
  for pos in range(len(rows[0])):
    most_common = get_most_common(rows, pos)
    value+=most_common
    rows = [row for row in rows if row[pos] == most_common]
    
  return int(value, 2)

def get_scrubber(rows):
  rows = rows[:]
  value = ''
  for pos in range(len(rows[0])):
    least_common = get_least_common(rows, pos)
    value+=least_common
    rows = [row for row in rows if row[pos] == least_common]
    
  return int(value, 2)

def solve():
  rows = [line.strip() for line in sys.stdin]
  return get_oxygen(rows)*get_scrubber(rows)

print solve()
