import sys
from string import ascii_lowercase

graph = []
start_x, start_y = 0,0

def map_letter(letter):
  return ascii_lowercase.find(letter)

for index, line in enumerate(sys.stdin):
  line = line.strip()
  graph.append([char for char in line])

  if 'E' in line:
    start_y = index
    start_x = line.find('E')
    graph[-1][start_x] = 'z'

  graph[-1] = [map_letter(letter) for letter in graph[-1]]

VISITED = '.'
index = 0
queue = []
queue.append((0, map_letter('z'), start_y, start_x))
while True:
  if index == len(queue):
    break
  dist, current_letter, y, x = queue[index]
  if current_letter == map_letter('a'):
    print(dist)
    break

  index += 1

  if graph[y][x] == VISITED:
    continue
  graph[y][x] = VISITED

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
