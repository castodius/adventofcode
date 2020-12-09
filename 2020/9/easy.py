import sys

PREAMBLE = 25

values = []

def verify(value):
  for i1, v1 in enumerate(values):
    for i2, v2 in enumerate(values):
      if i1 >= i2:
        continue
      if v1+v2 == value:
        return True

  return False

for line in sys.stdin:
  value = int(line)
  if len(values) != 25:
    values.append(value)
    continue

  if not verify(value):
    print value
    break

  values = values[1:]
  values.append(value)
