import sys

KEY = 'shiny gold bag'

graph = {}
def update_graph(bag_type, line):
  graph[bag_type] = []
  if line == 'no other bag':
    return
  bags = line.split(', ')
  for bag in bags:
    graph[bag_type].append(bag[2:])

def holds_bag_type(bag_type, search_key):
  for key in graph[bag_type]:
    if key == search_key or holds_bag_type(key, search_key):
      return True
  return False

types = set()
for line in sys.stdin:
  line = line.strip().replace('bags', 'bag').replace('.', '')
  bag, line = line.split(' contain ')
  update_graph(bag, line)
  types.add(bag)

seen = set()
count = 0
for bag_type in types:
  if holds_bag_type(bag_type, KEY):
    count += 1

print count