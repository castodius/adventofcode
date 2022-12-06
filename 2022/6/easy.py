import sys

transmission = sys.stdin.readline().strip()

for index in range(len(transmission)):
  s = set(transmission[index:index+4])
  if len(s) == 4:
    print (index + 4)
    break