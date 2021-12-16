import sys

LITERAL = 4

BITS = {
  0: 15,
  1: 11
}
FIFTEEN_BITS = 0
ELEVEN_BITS = 1

def get_binary():
  line = sys.stdin.readline()
  binary = bin(int(line, 16))[2:]
  
  l = len(binary)
  if l%4 != 0:
    binary = '0'*(4-l%4) + binary

  return binary

def unpack(s):
  print s
  version = int(s[:3], 2)
  print version
  type = int(s[3:6], 2)
  if type == LITERAL:
    return version
  else:
    I = int(s[6])
    bits = BITS[I]
    L = s[7:7+bits]
    L = int(L, 2)

    total = version
    index = 7+bits
    while index < len(s):
      remaining = s[index:]
      if len(remaining) == remaining.count('0'):
        return total

      bits = BITS[int(s[index],2)]
      if bits == 15:
        index+=1

      total += unpack(s[index:index+bits])
      index+=bits-1
    return total

def solve():
  binary = get_binary()
  return unpack(binary)

print solve()
