import sys

MASK = 'mask'
FLOATING = 'X'

# stupid but easy to follow
def get_indexes(mask, value):
  binary = bin(value)[2:]
  binary = '0'*(len(mask)-len(binary))+binary
  pattern = ''
  for index, bit in enumerate(mask):
    if bit == '0':
      pattern += binary[index]
    else:
      pattern += bit

  indexes = []
  exponent = pattern.count(FLOATING)
  for replacement in range(2**exponent):
    curr = pattern
    while curr.count(FLOATING) > 0:
      bit = replacement & 1
      if bit == 1:
        curr = curr.replace(FLOATING, '1', 1)
      else:
        curr = curr.replace(FLOATING, '0', 1)
      replacement >>= 1
    indexes.append(int(curr, 2))

  return indexes

mem = {}
for line in sys.stdin:
  action, value = line.strip().split(' = ')
  if action == MASK:
    mask = value
    continue

  address = int(action.split('[')[1][:-1])
  indexes = get_indexes(mask, address)
  for index in indexes:
    mem[index] = int(value)

print sum(mem.values())
#print sum(mem)
