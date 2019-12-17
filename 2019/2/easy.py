import sys

def solve(arr):
  pos = 0
  while True:
    if arr[pos] == 99:
      break
    op, pos1, pos2, res = arr[pos:pos+4]
    val1, val2 = arr[pos1], arr[pos2]
    if op == 1:
      arr[res] = val1+val2
    elif op == 2:
      arr[res] = val1*val2
    
    pos+=4
  
  return arr

for line in sys.stdin:
  data = map(int, line.split(','))
  data[1] = 12
  data[2] = 2
  print solve(data)[0]
