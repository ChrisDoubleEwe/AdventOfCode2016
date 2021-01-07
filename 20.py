import re
from printf import printf

ranges = []
blocked = []

with open("20_input.txt") as f:
  for line in f:
    line_split = line.strip().split('-')
    min = line_split[0]
    max = line_split[1]
    pair = []
    pair.append(int(min))
    pair.append(int(max))
    ranges.append(pair)


allowed = []

guess = 1

while guess < 4294967296:
  caught = 0
  for x in ranges:
    min = x[0]
    max = x[1]

    if guess >= min and guess <= max:
      guess = max+1
      caught = 1

  if caught == 0:
    allowed.append(guess)
    guess += 1

min_allowed = 4294967296
for x in allowed:
  if x < min_allowed:
    min_allowed = x

print "Part 1: " + str(min_allowed)
print "Part 2: " + str(len(allowed))
