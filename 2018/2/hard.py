import sys

lines = [line.strip() for line in sys.stdin]

def solve():
  for l1 in lines:
    for l2 in lines:
      if l1 == l2:
        continue
      count = 0
      same = []
      for i in range(len(l1)):
        if l1[i] != l2[i]:
          count += 1
        else:
          same.append(l1[i])
        
        if count > 1:
          break
      else:
        return same

ans = solve()
print ''.join(ans)