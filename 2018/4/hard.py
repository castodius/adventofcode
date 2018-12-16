import sys

lines = sorted([line.strip() for line in sys.stdin])

guards = {}

guard = -1
first = 0
for line in lines:
  curr = int(line.split(':')[1].split(']')[0])
  if 'Guard' in line: # new guard
    guard = int(line.split('#')[1].split(' ')[0])
    if guard not in guards:
      guards[guard] = [0]*60
  elif 'falls' in line:
    first = curr
  else:
    for i in range(first, curr):
      guards[guard][i]+=1

g = -1
m = 0
minute = -1
for guard, minutes in guards.iteritems():
  guard_max = max(minutes)
  if guard_max > m:
    g = guard
    m = guard_max
    minute = minutes.index(m)

print g * minute
