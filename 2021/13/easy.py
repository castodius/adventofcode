import sys

def fold_paper(points, fold):
  dir = fold["dir"]
  value = fold["value"]
  new_points = set()
  for x,y in points:
    if dir == "x":
      new_points.add((value - abs(value-x),y))
    else:
      new_points.add((x, value - abs(value-y)))

  return new_points

def solve():
  lines = [line.strip() for line in sys.stdin]

  points = set()
  for line in lines:
    if line == '':
      break
    x,y = map(int, line.split(','))
    points.add((x,y))

  folds = []
  for line in lines[len(points)+1:]:
    tmp = line.split(' ')[2]
    dir,value = tmp.split('=')
    value = int(value)
    folds.append({
      "dir": dir,
      "value": value
    })

  return len(fold_paper(points, folds[0]))
print solve()
