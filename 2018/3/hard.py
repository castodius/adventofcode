import sys

side = 1200
m = [[0 for i in range(side)] for j in range(side)]

counts = {}
for line in sys.stdin:
  inp = line.strip().split(' ')
  id = int(inp[0].strip('#'))
  x,y = map(int, inp[2].strip(':').split(','))
  sx,sy = map(int, inp[3].split('x'))
  counts[id] = sx*sy

  for cx in range(x,x+sx):
    for cy in range(y,y+sy):
      if m[cx][cy] != 0:
        m[cx][cy] = -1
      else:
        m[cx][cy] = id
        
for i in range(side):
  for j in range(side):
    value = m[i][j]
    if value == -1 or value == 0:
      continue
    counts[value] -= 1

for k,v in counts.iteritems():
  if v == 0:
    print k
