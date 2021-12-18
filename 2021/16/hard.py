import sys

LITERAL = 4

BITS = {
  0: 15,
  1: 11
}

TOTAL_LENGTH = 0
TOTAL_PACKETS = 1

SUM = 0
PRODUCT = 1
MINIMUM = 2
MAXIMUM = 3
GT = 5
LT = 6
EQUAL = 7

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
    return (index, int(total, 2))
  else:
    I = int(binary[index])
    index += 1
    packets = []
    if I == TOTAL_LENGTH:
      max_index = index + 15 + int(binary[index:index+15], 2)
      index += 15
      while index < max_index:
        index, value = solve(index)
        packets.append(value)
    else:
      packet_count = int(binary[index:index+11], 2)
      index += 11
      for _ in range(packet_count):
        index, value = solve(index)
        packets.append(value)

    ans = 0
    if type == SUM:
      ans = sum(packets)
    elif type == PRODUCT:
      ans = 1
      for value in packets:
        ans *= value
    elif type == MINIMUM:
      ans = min(packets)
    elif type == MAXIMUM:
      ans = max(packets)
    elif type == GT:
      ans = 1 if packets[0] > packets[1] else 0
    elif type == LT:
      ans = 1 if packets[0] < packets[1] else 0
    elif type == EQUAL:
      ans = 1 if packets[0] == packets[1] else 0

    return (index, ans)

binary = get_binary()
print solve(0)[1]
