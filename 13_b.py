import re
from printf import printf

number = 1364

map = []
map_size = 1000

for x in range(0, map_size):
  row = []
  for y in range(0, map_size):
    row.append('.')
  map.append(row)
    
for x in range(0, map_size):
  for y in range(0, map_size):
    square = (x*x)+(3*x)+(2*x*y)+y+(y*y)
    square += number
    b = str(bin(square))[2:]
    count = b.count('1')
    if count%2 == 1:
      map[y][x] = '#'
    else:
      map[y][x] = '.'

map[1][1] = 0

def print_map():
  for y in range(0, map_size):
    for x in range(0, map_size):
      printf(str(map[y][x]))
    print('')

def next_move():
  for y in range(0, map_size):
    for x in range(0, map_size):
      if map[y][x] != '.' and map[y][x] != '#':
        val = map[y][x]
        val += 1
        if val <= 50:
          if y > 0:
            if map[y-1][x] == '.':
              map[y-1][x] = val
          if y < map_size-1:
            if map[y+1][x] == '.':
              map[y+1][x] = val
          if x > 0:
            if map[y][x-1] == '.':
              map[y][x-1] = val
          if x < map_size-1:
            if map[y][x+1] == '.':
              map[y][x+1] = val
 

iter = 0
while iter < 60:
  iter += 1
  next_move()

count = 0
for x in range(0, map_size):
  for y in range(0, map_size):
    if map[y][x] != '.' and map[y][x] != '#':
      count += 1

print count
 
