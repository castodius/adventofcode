import sys
import string

poly = sys.stdin.readline()

alpha = string.ascii_lowercase
change = True
while change:
  length = len(poly)
  for letter in alpha:
    a = letter+letter.upper()
    poly = poly.replace(a, '')
    
    b = letter.upper()+letter
    poly = poly.replace(b, '')

  change = len(poly) != length #updates!

print len(poly)