import sys
from queue import PriorityQueue

VISITED = -1
deltas = [[0,1], [1,0], [0,-1], [-1,0]]

def solve():
  cave = [[int(c) for c in line.strip()] for line in sys.stdin]
  max_y = len(cave)
  max_x = len(cave[0])
  goal_y = max_y-1
  goal_x = max_x-1

  q = PriorityQueue()
  q.put((0, 0, (0,0)))
  while not q.empty():
    distance, cost, point = q.get()
    x,y = point
    if cave[y][x] == VISITED:
      continue
    #print cost, distance, point
    if y == goal_y and x == goal_x:
      return distance+cost
    cave[y][x] = VISITED

    for dx, dy in deltas:
      new_y = y+dy
      new_x = x+dx
      if new_y < 0 or new_y == max_y or new_x < 0 or new_x == max_x:
        continue
      value = cave[new_y][new_x]
      if value == VISITED:
        continue
      q.put((distance+cost, cave[new_y][new_x], (new_x, new_y)))
    

print solve()
