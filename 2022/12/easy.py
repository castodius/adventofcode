import sys
from string import ascii_lowercase

graph = []
start_x, start_y = 0,0
end_x, end_y = 0,0

def map_letter(letter):
  return ascii_lowercase.find(letter)

for index, line in enumerate(sys.stdin):
  line = line.strip()
  graph.append([char for char in line])

  if 'S' in line:
    start_y = index
    start_x = line.find('S')
    graph[-1][end_x] = 'a'

  if 'E' in line:
    end_y = index
    end_x = line.find('E')
    graph[-1][end_x] = 'z'

  graph[-1] = [map_letter(letter) for letter in graph[-1]]

VISITED = '.'
index = 0
queue = []
#visited = [[False]*len(graph[0]) for _ in range(len(graph))]
queue.append((0, 0, start_y, start_x))
while True:
  if index == len(queue):
    break
  dist, current_letter, y, x = queue[index]
  if y == end_y and x == end_x:
    print(dist)
    break

  index += 1

  if graph[y][x] == VISITED:
    continue
  graph[y][x] = VISITED
#  visited[y][x] = True

  for dy, dx in [[1,0], [0,1], [-1,0], [0,-1]]:
    tmp_x = x + dx
    tmp_y = y + dy
    if tmp_x < 0 or tmp_x == len(graph[0]):
      continue
    if tmp_y < 0 or tmp_y == len(graph):
      continue

    graph[tmp_y]
    letter = graph[tmp_y][tmp_x]
    if letter == VISITED:
      continue

    if letter - 1 <= current_letter <= letter +1:
      queue.append((dist+1, letter, tmp_y, tmp_x))

#for line in visited:
#  print(''.join(map(lambda x: '.' if x else 'X', [c for c in line])))