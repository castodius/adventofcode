time = int(raw_input())
data = raw_input().strip().split(',')
data = [int(element) for element in data if element != 'x']

best_distance = 1000000
best = 0

for value in data:
  remainder = time % value
  if remainder == 0:
    best_distance = 0
    best = time * value
    break

  distance = value - remainder
  if distance > best_distance:
    continue

  best_distance = distance
  best = value * distance

print best