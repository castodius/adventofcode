import sys

def foo(n):
  return n*(n+1)/2

def solve():
  crabs = map(int, sys.stdin.readline().split(','))
  fr = min(crabs)
  to = max(crabs)

  best = 10**9
  for value in range(fr, to):
    total = 0
    for crab in crabs:
      total += foo(abs(crab-value))

    best = min(best, total)
  return best

print solve()
