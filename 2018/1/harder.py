import sys

lines = [line for line in sys.stdin]

total = 0
seen = set()
seen.add(total)

count = 0
while True:
  index = count % len(lines)
  count += 1

  line = lines[index]
  value = int(line[1:])
  if '+' in line:
    total+=value
  else:
    total-=value
  
  if total in seen:
    print total
    break
  seen.add(total)
    
#print seen