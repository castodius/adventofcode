import sys

LITERAL = 4

BITS = {
  0: 15,
  1: 11
}

TOTAL_LENGTH = 0
TOTAL_PACKETS = 1

def get_binary():
  line = sys.stdin.readline()
  binary = bin(int(line, 16))[2:]
  
  l = len(binary)
  if l%4 != 0:
    binary = '0'*(4-l%4) + binary

  return binary

def solve(index):
  version = int(binary[index:index+3], 2)
  index += 3
  type = int(binary[index:index+3], 2)
  index += 3
  if type == LITERAL:
    total = ''
    while True:
      end = binary[index] == '0'
      total += binary[index+1:index+5]
      index += 5
      if end:
        break
    return (index, version)
  else:
    I = int(binary[index])
    index += 1
    total = version
    if I == TOTAL_LENGTH:
      max_index = index + 15 + int(binary[index:index+15], 2)
      index += 15
      while index < max_index:
        index, value = solve(index)
        total += value
    else:
      packets = int(binary[index:index+11], 2)
      index += 11
      for _ in range(packets):
        index, value = solve(index)
        total += value
    return (index, total)

binary = get_binary()
print solve(0)[1]
