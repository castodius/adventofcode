import sys
import math

def calc_fuel(n):
  return int(math.floor(n/3)-2)

def solve(n):
  total = 0
  fuel = calc_fuel(n)
  while fuel > 0:
    total+=fuel
    fuel = calc_fuel(fuel)
  return total

print sum([solve(int(line)) for line in sys.stdin])
    