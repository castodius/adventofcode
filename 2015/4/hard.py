import hashlib

data = raw_input().strip()

value = 1
while True:
  output = hashlib.md5(data + str(value)).hexdigest()
  if output.startswith('000000'):
    print value
    break
  value+=1