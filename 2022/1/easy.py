import sys

foo = lambda x: sum([int(value) for value in x.split('\n')])
sums = [foo(value) for value in sys.stdin.read().split('\n\n')]

print(max(sums))

sums.sort(reverse=True)
print(sum(sums[0:3]))
