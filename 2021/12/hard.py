import sys
from collections import defaultdict

START = 'start'
END = 'end'

small_used = False

def count_twos(dict):
  return dict.values().count(2)

def count_paths(current, graph,  visited):
  if current == END:
    return 1
  if visited[current] == 2:
    return 0

  is_small = current.lower() == current
  if is_small:
    visited[current] += 1
    if count_twos(visited) == 3: #more than one small cave visited twice
      visited[current] -= 1
      return 0
  
  total = 0
  for neighbor in graph[current]:
    total += count_paths(neighbor, graph, visited)

  if is_small:
    visited[current] -= 1
  return total

def solve():
  paths = [line.strip().split('-') for line in sys.stdin]
  graph = {}
  for src, dst in paths:
    if not src in graph:
      graph[src] = []
    graph[src].append(dst)
    if not dst in graph:
      graph[dst] = []
    graph[dst].append(src)

  visited = defaultdict(lambda: 0)
  visited[START] = 1

  return count_paths(START, graph, visited)

print solve()
