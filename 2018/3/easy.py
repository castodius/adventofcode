import sys

side = 1200
m = [[0 for i in range(side)] for j in range(side)]

count = 0
for line in sys.stdin:
  inp = line.strip().split(' ')
  x,y = map(int, inp[2].strip(':').split(','))
  sx,sy = map(int, inp[3].split('x'))

  for cx in range(x,x+sx):
    for cy in range(y,y+sy):
      m[cx][cy] += 1
      if(m[cx][cy]==2):
        count+=1

print count
