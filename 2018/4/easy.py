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
for guard, minutes in guards.iteritems():
  asleep = sum(minutes)
  if asleep > m:
    g = guard
    m = asleep

minutes = guards[g]
print g * minutes.index(max(minutes))
