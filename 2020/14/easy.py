import sys

CAP = 10**6

# stupid but easy to follow
def calc(mask, value):
  mask = mask[::-1]
  value = bin(value)[2:][::-1]

  tmp = ''
  for index, mask_bit in enumerate(mask):
    bit = '0'
    if index < len(value):
      bit = value[index]
    if mask_bit == 'X':
      tmp += bit
    else:
      tmp += mask_bit

  return int(tmp[::-1], 2)

mem = [0]*CAP
mask = ''
for line in sys.stdin:
  action, value = line.strip().split(' = ')
  if action == 'mask':
    mask = value
    continue

  value = calc(mask, int(value))
  index = int(action.split('[')[1][:-1])
  mem[index] = value

print sum(mem)