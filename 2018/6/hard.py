import sys

limit = 10000
edge = 1000

coords = [map(int, line.split(',')) for line in sys.stdin]
coords = [[x+500, y+500] for x,y in coords]

def in_range(x,y):
  total = 0
  for cx,cy in coords:
    total += abs(cx-x)+abs(cy-y)
    if total >= limit:
      return False

  return True

count = 0
for i in range(edge):
  for j in range(edge):
    if in_range(i,j):
      count+=1

print count