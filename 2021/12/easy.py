import sys

START = 'start'
END = 'end'

def count_paths(current, graph,  visited):
  if current == END:
    return 1
  if current in visited:
    return 0
  if current.lower() == current:
    visited.add(current)
  
  total = 0
  for neighbor in graph[current]:
    total += count_paths(neighbor, graph, visited)

  if current in visited:
    visited.remove(current)
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

  return count_paths(START, graph, set())

print solve()
