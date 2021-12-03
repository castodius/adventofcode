import sys

def solve():
  rows = [line.strip() for line in sys.stdin]
  gamma = epsilon = ''
  for position in range(len(rows[0])):
    values = [row[position] for row in rows]
    ones = values.count('1')
    zeroes = values.count('0')
    gamma += '1' if ones > zeroes else '0'
    epsilon += '0' if ones > zeroes else '1'

  return int(gamma, 2)* int(epsilon, 2)

print solve()
