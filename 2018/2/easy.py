import sys

alpha = 'qwertyuiopasdfghjklzxcvbnm'

counts = [0]*10
for line in sys.stdin:
  for i in range(2,4):
    counts[i] += 1 if any([True for letter in alpha if i==line.count(letter)]) else 0

print counts[2]*counts[3]