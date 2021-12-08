import sys

def get_value(arr):
  keys = arr["keys"]
  keys.sort(key=len)
  keys = [''.join(sorted(key)) for key in keys]
  by_key = {
    keys[0]: 1,
    keys[1]: 7,
    keys[2]: 4,
    keys[9]: 8
  }
  by_value = {
    1: keys[0],
    7: keys[1],
    4: keys[2],
    8: keys[9],
  }

  fives = keys[3:6]
  sixes = keys[6:9]
  
  # find 3 via 1
  one = by_value[1]
  for index, five in enumerate(fives):
    for chr in one:
      if not (chr in five):
        break
    else:
      by_key[five] = 3
      by_value[3] = five
      del fives[index]
      break

  # find 5 via 4, they share three lines
  two, five = fives
  total = 0
  for chr in by_value[4]:
    if chr in five:
      total += 1
  if total == 2:
    two, five = five, two
  
  by_key[two] = 2
  by_value[2] = two
  by_key[five] = 5
  by_value[5] = five
  
  # find 6 via 1
  for index, six in enumerate(sixes):
    for chr in one:
      if not (chr in six):
        by_key[six] = 6
        by_value[6] = six
        del sixes[index]
        break

  # find 9 via 4, 4 is a subset of 9
  zero, nine = sixes
  total = 0
  for chr in by_value[4]:
    if chr in nine:
      total += 1
  if total != 4:
    zero, nine = nine, zero
  
  by_key[nine] = 9
  by_value[9] = nine
  by_key[zero] = 0
  by_value[0] = zero

  ans = 0
  for value in arr["values"]:
    ans *= 10
    value = ''.join(sorted(value))
    ans += by_key[value]
  return ans

def solve():
  data = []
  for line in sys.stdin:
    keys, values = line.split('|')
    keys = keys.strip().split(' ')
    values = values.strip().split(' ')
    data.append({
      "keys": keys,
      "values": values
    })

  total = 0
  for line in data:
    total += get_value(line)

  return total
print solve()
