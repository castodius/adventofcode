import sys

KEY = 'shiny gold bag'

graph = {}
def update_graph(bag_type, line):
  graph[bag_type] = []
  if line == 'no other bag':
    return
  bags = line.split(', ')
  for bag in bags:
    graph[bag_type].append({
      'count': int(bag[0]),
      'type': bag[2:]
    })

def count_bag_type(bag_type):
  if len(graph[bag_type]) == 0:
    return 0

  count = 0
  for bag_object in graph[bag_type]:
    count += bag_object['count']
    count += bag_object['count']*count_bag_type(bag_object['type'])

  return count

for line in sys.stdin:
  line = line.strip().replace('bags', 'bag').replace('.', '')
  bag, line = line.split(' contain ')
  update_graph(bag, line)

print count_bag_type(KEY)