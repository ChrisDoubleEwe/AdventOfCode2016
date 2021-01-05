import re
from printf import printf
import hashlib

row = '.^^.^.^^^^'
row = '^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^.......'

rows = []


old_row = row
rows.append(row)


def get_char(row, x):
  l = ''
  c = ''
  r = ''
  if x == 0:
    l = '.'
  else:
    l = row[x-1]
  c = row[x]
  if x == len(row)-1:
    r = '.'
  else:
    r = row[x+1]
  if l == c == '^' and r == '.':
    return '^'
  if r == c == '^' and l == '.':
    return '^'
  if r == c == '.' and l == '^':
    return '^'
  if l == c == '.' and r == '^':
    return '^'
  return '.'

    
def get_new_row(r):
  new_row = ''
  for x in range(0, len(r)):
    new_row += get_char(r, x)
  return new_row
    
for i in range(1, 40):
  new_row = get_new_row(old_row)
  rows.append(new_row)
  old_row = new_row
 
count = 0
for z in rows:
  count += z.count('.')
print count
