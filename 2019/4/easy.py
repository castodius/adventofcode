import sys

def check_double(n):
  s = str(n)
  return any([True for i in s if s.count(i)>=2])

def check_ascending(n):
  s = str(n)
  curr = s[0]
  for i in s[1:]:
    if curr > i:
      return False
    curr = i
  return True

def good_value(n):
  return check_double(n) and check_ascending(n)

def solve(low, high):
  return sum([1 for n in range(low, high+1) if good_value(n)])
    

low, high = map(int, sys.stdin.readline().split('-'))
print solve(low, high)