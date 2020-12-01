import sys

def solve():
  years = []
  for line in sys.stdin:
    years.append(int(line))

  for index, y1 in enumerate(years):
    for index2, y2 in enumerate(years):
      if index == index2:
        continue
      if y1+y2 == 2020:
        return y1*y2

print solve()