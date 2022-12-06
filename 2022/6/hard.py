import sys

transmission = sys.stdin.readline().strip()

for index in range(len(transmission)):
  s = set(transmission[index:index+14])
  if len(s) == 14:
    print (index + 14)
    break
