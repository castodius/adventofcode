import sys

MAX_SECONDS = 30
NOT_CALCULATED = -1

graph_index = 0
mappings = {}
graph = []

flows = {}

mask_shift = 1
masks = {}

def get_point_index(point):
  global graph_index
  if not point in mappings:
    mappings[point] = graph_index
    graph.append([])
    graph_index += 1
  return mappings[point]

for line in sys.stdin:
  line = line.strip()
  
  source = line.split(' ')[1]
  source_index = get_point_index(source)
  source = mappings[source]
  
  flow = int(line.split(' ')[4].split('=')[1][:-1])
  if flow != 0:
    flows[source_index] = flow
    masks[source_index] = mask_shift
    mask_shift <<= 1

  if 'valves' in line:
    destinations = line.split('valves ')[1].split(', ')
  else:
    destinations = line.split('valve ')[1].split(', ')

  for destination in destinations:
    destination_index = get_point_index(destination)
    graph[source_index].append(destination_index)

calculations = [[[NOT_CALCULATED]*mask_shift for j in range(len(graph))] for i in range(MAX_SECONDS)]

def solve(seconds, point, enabled_flows):
  if seconds == MAX_SECONDS:
    return 0
  
  calculated = calculations[seconds][point][enabled_flows]
  if calculated != NOT_CALCULATED:
    return calculated

  max_flow = 0
  if point in flows and not enabled_flows & masks[point]:
    point_flow = (MAX_SECONDS - seconds - 1)*flows[point]
    total_flow = point_flow + solve(seconds + 1, point, enabled_flows ^ masks[point])
    max_flow = max(max_flow, total_flow)

  for neighbor in graph[point]:
    max_flow = max(max_flow, solve(seconds + 1, neighbor, enabled_flows))

  calculations[seconds][point][enabled_flows] = max_flow
  
  return max_flow

print(solve(0, mappings['AA'], 0))
