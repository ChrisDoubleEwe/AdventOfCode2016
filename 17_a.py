import re
from printf import printf
import hashlib

passcode = 'hijkl'
passcode = 'ihgpwlah'
passcode = 'kglvqrro'
passcode = 'ulqzkmiv'
passcode = 'rrrbmfta'


shortest = 999
all_routes = []
x = 1
y = 1

a = []
a.append('##########')
a.append('# | | | ##')
a.append('#-#-#-#-##')
a.append('# | | | ##')
a.append('#-#-#-#-##')
a.append('# | | | ##')
a.append('#-#-#-#-##')
a.append('# | | |  #')
a.append('####### V#')
a.append('##########')
 
map = []
for row in a:
  map_row = []
  for c in row:
    map_row.append(c)
  map.append(map_row)


def move(p, me_x, me_y):
  global shortest
  if len(p) > shortest:
    return
  possible_moves = []

  if me_y == 7 and me_x == 7:
    all_routes.append(p)
    if len(p) < shortest:
      shortest = len(p)

  md = hashlib.md5(p.encode('utf-8')).hexdigest()
  if map[me_y-1][me_x] == '-' and md[0] in 'bcdef':
    possible_moves.append('U')
  if map[me_y+1][me_x] == '-' and md[1] in 'bcdef':
    possible_moves.append('D')
  if map[me_y][me_x-1] == '|' and md[2] in 'bcdef':
    possible_moves.append('L')
  if map[me_y][me_x+1] == '|' and md[3] in 'bcdef':
    possible_moves.append('R')

  for m in possible_moves:
    if m == 'U':
      move(p+m, me_x, me_y-2)
    if m == 'D':
      move(p+m, me_x, me_y+2)
    if m == 'L':
      move(p+m, me_x-2, me_y)
    if m == 'R':
      move(p+m, me_x+2, me_y)





 
move(passcode, x, y)

for i in all_routes:
  if len(i) == shortest:
    for c in i:
      if c in 'UDLR':
        printf(c)

print

