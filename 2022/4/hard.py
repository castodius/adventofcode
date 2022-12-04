import sys

jobs = [job.strip().split(',') for job in sys.stdin]

unpack = lambda x: map(int, x.split('-'))
ans = 0
for job in jobs:
  start_1, end_1 = unpack(job[0])
  start_2, end_2 = unpack(job[1])

  s1 = set([value for value in range(start_1, end_1+1)])
  s2 = set([value for value in range(start_2, end_2+1)])

  if s1 & s2:
    ans += 1

print(ans)