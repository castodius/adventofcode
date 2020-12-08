import sys

instructions = []
for line in sys.stdin:
  action, value = line.strip().split(' ')
  value = int(value)
  instructions.append({
    'action': action,
    'value': value
  })


prev = 0
curr = 0
index = 0
vis = set()
while True:
  if index in vis:
    print prev
    break

  prev = curr
  vis.add(index)
  obj = instructions[index]
  action = obj['action']
  value = obj['value']

  if action == 'nop':
    index+=1
  elif action == 'acc':
    index+=1
    curr += value
  else:
    index += value