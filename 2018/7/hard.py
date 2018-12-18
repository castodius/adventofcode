import sys
import string

workers = 5
overhead = 60

alpha = string.ascii_uppercase
letters = {}
time_left = {}

for letter in alpha:
  letters[letter] = []
  time_left[letter] = overhead+alpha.index(letter)+1

active = set()
for line in sys.stdin:
  values = line.split(' ')
  letters[values[7]].append(values[1])
  active.add(values[7])
  active.add(values[1])
left = len(active) #the number of tasks to complete

def remove_reference(worker): #removes all references to a worker from all "queues"
  for letter in alpha:
    if letter not in active:
      continue
    
    if worker in letters[letter]:
      index = letters[letter].index(worker)
      del letters[letter][index]

order = []
assigned = []
seconds = 0

while True:
  if len(assigned) > 0:
    seconds += 1
  
  for worker in reversed(assigned): #downtick each worker
    time_left[worker]-=1
    if time_left[worker] == 0: #work done? add to pool, remove from active, remove from all references
      index = assigned.index(worker)
      del assigned[index]
      remove_reference(worker)
      left -= 1
      workers += 1

  if left == 0:
    break

  for letter in alpha:
    if workers == 0:
      break

    if letter not in active:
      continue
    
    if len(letters[letter]) == 0:
      workers -= 1
      assigned.append(letter)
      active.remove(letter)

print seconds