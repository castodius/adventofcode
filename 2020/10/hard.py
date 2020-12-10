import sys

adapters = [int(line) for line in sys.stdin]
adapters.sort()
MIN = 0
MAX = max(adapters) + 3

def find_gaps():
  ans = []

  prev = adapters[0]
  curr = []
  curr.append(prev)
  for adapter in adapters[1:]:
    if adapter - prev == 3:
      ans.append(curr)
      curr = []
    
    curr.append(adapter)
    prev = adapter

  ans.append(curr)
  return ans

def get_all_lists(l):
  exp = len(l)
  ans = []
  for i in range(0, 2**exp - 1):
    tmp = l[:]
    index = 0
    while i != 0:
      if i & 1 == 1:
        del tmp[index]
        index -= 1
      i >>= 1
      index += 1
    ans.append(tmp)

  return ans

def count_combos(gap):
  mn = min(gap)
  first = mn <= 3 # first gap
  if first:
    low = 0
  else:
    low = mn -3
  high = max(gap)+3

  lists = get_all_lists(gap)

  count = 0
  for l in lists:
    if low + 3 < l[0]:
      continue
    if high -3 > l[-1]:
      continue
    prev = l[0]
    for value in l:
      if prev + 3 < value:
        break
      prev = value
    else:
      count += 1
  return count

gaps = find_gaps()

count = 1
for index, gap in enumerate(gaps):
  count *= count_combos(gap)

print count
