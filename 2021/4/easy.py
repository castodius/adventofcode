import sys

class Board:
  def __init__(self, rows):
    self.rows = rows
    self.marked = [[False for _ in range(5)] for a in range(5)]

  def hasWon(self):
    for row in self.marked:
      if row.count(True) == 5:
        return True

    for pos in range(len(self.marked[0])):
      values = [row[pos] for row in self.marked]
      if values.count(True) == 5:
        return True

    return False

  def mark(self, number):
    for a in range(5):
      for b in range(5):
        if self.rows[a][b] == number:
          self.marked[a][b] = True

    return self.hasWon()

  def countUnmarked(self):
    total = 0
    for index, row in enumerate(self.marked):
      for index2, value in enumerate(row):
        if value:
          continue
        total += self.rows[index][index2]

    return total

  def printState(self):
    print self.marked

boards = []

def processBoards(numbers):
  for number in numbers:
    for board in boards:
      result = board.mark(number)
      if result:
        return board.countUnmarked() * number

def solve():
  rows = [line.strip() for line in sys.stdin]
  numbers = map(int, rows[0].split(','))

  for index in range(2, len(rows), 6):
    board = [map(int, [value for value in row.split(' ') if value != '']) for row in rows[index:index+5]]
    boards.append(Board(board))

  return processBoards(numbers)

print solve()
