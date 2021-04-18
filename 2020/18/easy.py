import sys

PLUS = '+'
MINUS = '-'
MULTIPLY = '*'
DIVIDE = '/'

operators = [PLUS, MINUS, MULTIPLY, DIVIDE]

def calculate(left, operator, right):
  if operator == PLUS:
    return left + right
  if operator == MINUS:
    return left - right
  if operator == MULTIPLY:
    return left * right
  if operator == DIVIDE:
    return left / right

def solve_rec(arr):
  curr = 0
  operator = '+'
  within_expression = False
  parenthesis_count = 0
  new_arr = []
  for element in arr:
    if not within_expression and len(element) == 1:
      if element in operators:
        operator = element
      else:
        curr = calculate(curr, operator, int(element)) 
    else:
      if parenthesis_count == 0:
        within_expression = True
        parenthesis_count = element.count('(')
        new_arr.append(element[1:])
      else:
        parenthesis_count += element.count('(')
        parenthesis_count -= element.count(')')
        if parenthesis_count == 0:
          new_arr.append(element[:-1])
          curr = calculate(curr, operator, solve_rec(new_arr))
          new_arr = []
          within_expression = False
        else:
          new_arr.append(element)
  return curr


def solve(line):
  elements = line.strip().split(' ')
  return solve_rec(elements)

print sum([solve(line) for line in sys.stdin])
