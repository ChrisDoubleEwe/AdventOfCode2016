import re

def isAbba(z):
  for x in 'abcdefghijklmnopqrstuvwxyz':
    for y in 'abcdefghijklmnopqrstuvwxyz':
      if x == y:
        continue
      abba = x+y+y+x
      if abba in z:
        return True
  return False
 
def isAba(sup, hyp):
  for x in 'abcdefghijklmnopqrstuvwxyz':
    for y in 'abcdefghijklmnopqrstuvwxyz':
      if x == y:
        continue
      aba = x+y+x
      bab = y+x+y
      if aba in sup:
        if bab in hyp:
          return True
  return False

total = 0
total_aba = 0

with open("07_input.txt") as f:
  for line in f:
    this_abba = ''
    this_hypernet = ''
    in_abba = 1
    for c in line.strip():
      if c == '[':
        this_abba += '-'
        in_abba = 0
        continue
      if c == ']':
        this_hypernet += '-'
        in_abba = 1
        continue
      if in_abba == 1:
        this_abba += c
      else:
        this_hypernet += c

    if isAbba(this_abba):
      if not isAbba(this_hypernet):
        total += 1

    if isAba(this_abba, this_hypernet):
      total_aba += 1

print "Part one: " + str(total)
print "Part two: " + str(total_aba)

