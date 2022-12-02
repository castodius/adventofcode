import sys

ROCK = 0
PAPER = 1
SCISSORS = 2
them = {
  'A': ROCK,
  'B': PAPER,
  'C': SCISSORS
}
us = {
  'X': ROCK,
  'Y': PAPER,
  'Z': SCISSORS
}

result_points = [
  [3, 0, 6],
  [6, 3, 0],
  [0, 6, 3]
]

turns = [turn.split(' ') for turn in  sys.stdin.read().split('\n')]
turns = [(them[turn[0]], us[turn[1]]) for turn in turns]

result = sum([(result_points[turn[1]][turn[0]] + turn[1] + 1) for turn in turns])
print(result)

