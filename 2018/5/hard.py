import sys
import string

alpha = string.ascii_lowercase

def solve(poly):
  change = True
  while change:
    length = len(poly)
    for letter in alpha:
      a = letter+letter.upper()
      poly = poly.replace(a, '')
      
      b = letter.upper()+letter
      poly = poly.replace(b, '')

    change = len(poly) != length #updates!

  return len(poly)

poly = sys.stdin.readline()

print min([solve(poly.replace(letter, '').replace(letter.upper(), '')) for letter in alpha])