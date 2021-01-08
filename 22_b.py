import re
from printf import printf
import copy

nodes = []

lines = 0
max_x = 0
max_y = 0
with open("22_input.txt") as f:
  for line in f:
    lines += 1
    if lines < 3:
      continue
    line_split = line.strip().split(' ')
    row = []
    for a in line_split:
      if a != '':
        a = a.replace('/dev/grid/node-', '')
        a = a.replace('T', '')
        a = a.replace('%', '')
        if a.isdigit():
          a = int(a)
        row.append(a)
    match = re.search('x([0-9]*)-y([0-9]*)', row[0])
    x = int(match.group(1))
    y = int(match.group(2))
    if x > max_x:
      max_x = x
    if y > max_y:
      max_y = y

    row.append(x)
    row.append(y)

    nodes.append(row)

def print_map():
  for y in range(0, max_y+1):
    for x in range(0, max_x+1):
      if x == y == 0:
        printf('(' + map[y][x] + ')')
      else:
        printf(' ' + map[y][x] + ' ')
    print '' 


viable_nodes = []

sizes = []
used = []
for a in nodes:
  sizes.append(a[1])
  used.append(a[2])


smallest_size = min(sizes)

map = []
for y in range(0, max_y+1):
  this_row = []
  for x in range(0, max_x+1):
    this_row.append('.')
  map.append(this_row)

map[0][max_x] = 'G'
for a in nodes:
  if a[2] == 0:
    map[a[6]][a[5]] = '-'
  if a[2] > smallest_size:
    map[a[6]][a[5]] = '#'

print_map()

# Moves to get space adacent to Goal data (by inspection)
moves = 6 + 21 + 7

# Each move of goal left by 1 needs 5 moves:
# - Goal left (1)
# - Space down (1)
# - Space left (3)
# - Space up (1)

moves += 5 * 36

# and finally one move to get goal to 0,0
moves += 1

print moves

  



      

