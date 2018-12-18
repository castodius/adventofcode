import sys
import string

alpha = string.ascii_uppercase
letters = {}

for letter in alpha:
  letters[letter] = []

active = set()
for line in sys.stdin:
  values = line.split(' ')
  letters[values[7]].append(values[1])
  active.add(values[7])
  active.add(values[1])

order = []
changes = True

while changes:
  changes = False
  for letter in alpha:
    if letter not in active: #should be ignored
      continue
    
    if 0 == len(letters[letter]):
      order.append(letter)
      active.remove(letter) #no longer active

      for l2 in letters: #clear out all references
        if l2 not in active:
          continue
        
        if letter in letters[l2]:
          index = letters[l2].index(letter)
          del letters[l2][index]

      changes = True
      break
  

print ''.join(order)