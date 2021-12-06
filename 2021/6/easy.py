import sys

def solve():
  values = map(int, sys.stdin.readline().split(','))
  fish = [0]*9
  for value in values:
    fish[value]+=1

  for _ in range(80):
    new_fish = fish[0]
    for index in range(8):
      fish[index] = fish[index+1]
    fish[8] = new_fish
    fish[6] += new_fish
  return sum(fish)

print solve()
