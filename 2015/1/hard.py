data = raw_input().strip()

level = 0
for index, char in enumerate(data, 1):
  if char == '(':
    level += 1
  else:
    level -= 1
  
  if level == -1:
    print index
    break