import sys


class Monkey():
  def __init__(self):
    self.items = []
    self.items_inspected = 0

  def set_calming_factor(self, factor):
    self.calming_factor = factor

  def add_items(self, items):
    items = map(int, items.split(': ')[1].split(', '))
    for item in items:
      self.add_item(item)

  def add_item(self, item):
    self.items.append(item)

  def set_operation(self, operation):
    math = operation.split(' = ')[1]
    _, operator, value = math.split(' ')
    if value == 'old':
      if operator == '*':
        self.operation = lambda x: x * x
      else:
        self.operation = lambda x: x + x
    else:
      value = int(value)
      if operator == '*':
        self.operation = lambda x: x * value
      else:
        self.operation = lambda x: x + value

  def set_throwing_conditions(self, condition, true_statement, false_statement):
    self.divisor = int(condition.split(' ')[-1])
    self.true_monkey = int(true_statement.split(' ')[-1])
    self.false_monkey = int(false_statement.split(' ')[-1])

  def act(self):
    if len(self.items) == 0:
      return (None, None)
    
    self.items_inspected += 1
    item = self.items.pop(0)
    item = self.operation(item)
    item = item % self.calming_factor

    if item % self.divisor == 0:
      return (self.true_monkey, item)
    else:
      return (self.false_monkey, item)

data = sys.stdin.read().split('\n\n')
monkeys = []
calming_factor = 1
for row in data:
  attributes = row.split('\n')
  monkey = Monkey()
  monkey.add_items(attributes[1])
  monkey.set_operation(attributes[2])
  monkey.set_throwing_conditions(attributes[3], attributes[4], attributes[5])
  calming_factor *= monkey.divisor
  monkeys.append(monkey)
  
for monkey in monkeys:  
  monkey.set_calming_factor(calming_factor)

for round in range(10000):
  for monkey in monkeys:
    while True:
      target, item = monkey.act()
      if target == None:
        break

      monkeys[target].add_item(item)

inspections = [monkey.items_inspected for monkey in monkeys]
inspections.sort(reverse=True)
print(inspections[0] * inspections[1])
