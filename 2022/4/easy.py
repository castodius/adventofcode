import sys

jobs = [job.strip().split(',') for job in sys.stdin]

unpack = lambda x: map(int, x.split('-'))
ans = 0
for job in jobs:
  start_1, end_1 = unpack(job[0])
  start_2, end_2 = unpack(job[1])

  if start_1 >= start_2 and end_1 <= end_2:
    ans += 1
  elif start_1 <= start_2 and end_1 >= end_2:
    ans += 1

print(ans)