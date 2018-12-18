import sys
import Queue

coordinates = [map(int, line.split(',')) for line in sys.stdin]

maxx = max([coord[0] for coord in coordinates])
maxy = max([coord[1] for coord in coordinates])

m = [[(0, 0) for i in range(maxy)] for i in range(maxx)]

q = Queue.Queue()
index = 1
for coord in coordinates:
  x, y = coord
  q.put((x-1, y-1, index, 0)) #x,y, elem index, depth
  index+=1

deltas = [[0,1],[1,0],[0,-1],[-1,0]]
while not q.empty():
  x, y, elem, depth = q.get()
  curr, curr_depth = m[x][y]
  if curr == -1: #collision point, back off!
    continue

  if curr != 0: #something is here
    if depth == curr_depth and elem != curr: #another BFS running on the same depth and not the same element
      m[x][y] = (-1, depth) #collision point
    continue #if we come across which is not 0 then we have to continue
  
  m[x][y] = (elem, depth) #claim this spot!

  for delta in deltas:
    newx = x + delta[0]
    newy = y + delta[1]
    if newx < 0 or newx >= maxx:
      continue
    if newy < 0 or newy >= maxy:
      continue
    q.put((newx, newy, elem, depth+1))

skip = set()
skip.add(-1) # ignore collision

for index, _ in m[0]+m[-1]:
  skip.add(index)

for row in m:
  skip.add(row[0][0])
  skip.add(row[-1][0])

counts = {}
for row in m:
  for index, _ in row:
    if index in skip:
      continue
    if index not in counts:
      counts[index] = 1 #too lazy to find syntax for default value
    else:
      counts[index] +=1

print max([value for _,value in counts.iteritems()])