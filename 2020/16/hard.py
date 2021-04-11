import sys

class NumberContainer: # bad name is bad?
  def __init__(self):
    self.valid = set()

  def add(self, string_range):
    a, b = map(int, string_range.split('-'))
    for i in range(a, b+1):
      self.valid.add(i)

  def has_value(self, value):
    return value in self.valid

def update_ranges(container, row):
  row = row.split(': ')[1]
  range1, range2 = row.split(' or ')
  container.add(range1)
  container.add(range2)

def parse_ticket(row):
  return map(int, row.split(','))


def is_valid(container, row):
  values = parse_ticket(row)
  for value in values:
    if not container.has_value(value):
      return False
  return True

def get_valid_tickets():
  rows = [row.strip() for row in sys.stdin]
  container = NumberContainer()
  round = 0
  fields = []
  tickets = []
  my_ticket = []
  for row in rows:
    if row == '' or 'nearby' in row:
      round += 1
      continue
    if round == 0:
      fields.append(row)
      update_ranges(container, row)
    elif round == 1:
      if 'ticket' in row:
        continue
      my_ticket = parse_ticket(row)
    else:
      if is_valid(container, row):
        tickets.append(parse_ticket(row))
  
  return fields, tickets, my_ticket

def parse_range(s):
  return map(int, s.split('-'))

def parse_field(field): # if I was less lazy I would probably use this function when discarding invalid tickets
  name, tmp = field.split(': ')
  low, high = tmp.split(' or ')
  ranges = [parse_range(low), parse_range(high)]
  return name, ranges

def build_range(max):
  return [i for i in range(max)]

def value_in_range(range, value):
  return range[0] <= value <= range[1]

def get_field_positions(fields, tickets):
  fields = map(parse_field, fields)
  possible_positions = []
  for field in fields:
    possible = build_range(len(fields))
    name, ranges = field
    low, high = ranges
    for ticket in tickets:
      tmp_possible = []
      for value in possible:
        ticket_field = ticket[value]
        if value_in_range(low, ticket_field) or value_in_range(high, ticket_field):
          tmp_possible.append(value)

      possible = tmp_possible
    
    possible_positions.append(possible)

  positions = []
  while True:
    curr = 0
    for index, possible in enumerate(possible_positions):
      if len(possible) != 1:
        continue
      curr = possible[0]
      name = fields[index][0]
      positions.append([name, curr])
      break
    else:
      break

    for possible in possible_positions:
      if curr in possible:
        del possible[possible.index(curr)]
  return positions

fields, valid_tickets, my_ticket = get_valid_tickets()
positions = get_field_positions(fields, valid_tickets)

answer = 1
for name, position in positions:
  if not 'departure' in name:
    continue
  answer*=my_ticket[position]

print answer
