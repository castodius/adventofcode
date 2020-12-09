import sys

TARGET = 167829540

values = []

def verify(index):
  total = 0
  mn = 10**12
  mx = -1
  for value in values[index:]:
    total += value
    if total > TARGET:
      return False
    
    mn = min(mn, value)
    mx = max(mx, value)
    if total == TARGET:
      return mn + mx

  return False

for line in sys.stdin:
  value = int(line)
  values.append(value)
  
for index, _ in enumerate(values):
  output = verify(index)
  if output != False:
    print output
    break
