raw_input()
data = raw_input().strip().split(',')
data = [int(element) if element != 'x' else element for element in data]

curr = data[0]
multiplier = curr
for shift, value in enumerate(data[1:],1):
  if value == 'x':
    continue

  while (curr + shift) % value != 0:
    curr += multiplier
  multiplier*=value

print curr
