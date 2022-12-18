import sys

MAX_SECONDS = 26
NOT_CALCULATED = -1
ENABLE_FLOW = -2

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

calculations = [[[NOT_CALCULATED]*mask_shift for j in range(graph_index ** 2)] for i in range(MAX_SECONDS)]
all_flows_enabled = (2**mask_shift) - 1

def points_to_index(points):
  return points[0] * graph_index + points[1]

def solve(seconds, points, enabled_flows):
  if enabled_flows == all_flows_enabled:
    return 0

  if seconds == MAX_SECONDS:
    return 0
  
  index = points_to_index(points)
  calculated = calculations[seconds][index][enabled_flows]
  if calculated != NOT_CALCULATED:
    return calculated

  max_flow = 0
  point1, point2 = points
  for first_action in graph[point1] + [ENABLE_FLOW]:
    current_flow_point1 = 0
    local_enabled_flows_point1 = enabled_flows
    if first_action == ENABLE_FLOW:
      if not point1 in flows:
        continue
      if point1 in flows and enabled_flows & masks[point1]:
        continue
      local_enabled_flows_point1 = enabled_flows ^ masks[point1]
      current_flow_point1 = (MAX_SECONDS - seconds - 1) * flows[point1]

    for second_action in graph[point2] + [ENABLE_FLOW]:
      local_enabled_flows_point2 = local_enabled_flows_point1
      current_flow_point2 = 0
      if second_action == ENABLE_FLOW:
        if point1 == point2:
          continue
        if not point2 in flows:
          continue
        if point2 in flows and not local_enabled_flows_point1 & masks[point2]:
          local_enabled_flows_point2 = local_enabled_flows_point1 ^ masks[point2]
          current_flow_point2 = (MAX_SECONDS - seconds - 1) * flows[point2]

      new_point1 = first_action if first_action != ENABLE_FLOW else point1
      new_point2 = second_action if second_action != ENABLE_FLOW else point2
      new_points = (new_point1, new_point2) if new_point1 < new_point2 else (new_point2, new_point1)

      max_flow = max(max_flow, current_flow_point1 + current_flow_point2 + solve(seconds + 1, new_points, local_enabled_flows_point2))

  calculations[seconds][index][enabled_flows] = max_flow

  return max_flow

print(solve(0, (mappings['AA'], mappings['AA']), 0))