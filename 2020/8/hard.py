import sys

instructions = []

def run_program():
  index = 0
  curr = 0
  vis = set()
  while True:
    if index > len(instructions) - 1:
      return curr
    if index in vis:
      return False

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

def flip(index):
  if instructions[index]['action'] == 'nop':
    instructions[index]['action'] = 'jmp'
  else:
    instructions[index]['action'] = 'nop'

for line in sys.stdin:
  action, value = line.strip().split(' ')
  value = int(value)
  instructions.append({
    'action': action,
    'value': value
  })

for index in range(len(instructions)):
  if instructions[index]['action'] == 'acc':
    continue
  
  flip(index)
  ans = run_program()
  if ans != False:
    print ans
    break

  flip(index)
