import sys

def solve():
  years = []
  for line in sys.stdin:
    years.append(int(line))

  for index, y1 in enumerate(years):
    for index2, y2 in enumerate(years):
      for index3, y3 in enumerate(years):
        if index == index2 or index == index3 or index2 == index3:
          continue
        if y1+y2+y3 == 2020:
          return y1*y2*y3

print solve()