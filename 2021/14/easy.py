import sys

ITER = 10
LETTERS = ['B', 'N', 'C', 'H']

def solve():
  lines = [line.strip() for line in sys.stdin]
  state = lines[0]

  transitions = {}
  for line in lines[2:]:
    src, dst = line.split(' -> ')
    transitions[src] = dst

  for _ in range(ITER):
    new_state = ''
    for index in range(len(state)-1):
      key = state[index:index+2]
      new_state += key[0]+transitions[key]

    state = new_state + state[-1]

  counts = []
  for letter in LETTERS:
    counts.append((state.count(letter), letter))

  counts.sort()
  return counts[-1][0] - counts[0][0]

print solve()
