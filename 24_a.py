import re
from printf import printf
import copy
import itertools

map =  []
starts = {}
x = 0
y = 0
distances = []

with open("24_input.txt") as f:
  for line in f:
    y += 1
    row = []
    x = 0
    for c in line.strip():
      x += 1
      row.append(c)
    map.append(row)

      
def print_map():
  for i in range(0, y):
    for j in range(0, x):
      printf(map[i][j])
    print('')



max_num = -1
for i in range(0, y):
  for j in range(0, x):
    if map[i][j] in '0123456789':
      if int(map[i][j]) > max_num:
        max_num = int(map[i][j])
      coords = []
      coords.append(i)
      coords.append(j)
      starts[int(map[i][j])] = coords

map_x = x
map_y = y


for i in range(0, max_num+1):
  row = []
  for j in range(0, max_num+1):
    row.append(-1)
  distances.append(row)

def get_distance(i, j):
  print "+++ GETTING DISTANCE " + str(i) + " TO " + str(j)
  if i == j:
    return 0
  if distances[j][i] != -1:
    return distances[j][i] 
  mymap = copy.deepcopy(map)
  startx = starts[i][1]
  starty = starts[i][0]
  destx = starts[j][1]
  desty = starts[j][0]

  steps = 0
  mymap[starty][startx] = steps
  while True:
    this_map = copy.deepcopy(mymap)
    steps += 1
    for y in range(1, map_y-1):
      for x in range(1, map_x-1):
        if isinstance(mymap[y][x], int):
          if isinstance(mymap[y-1][x], basestring):
            if mymap[y-1][x] == '.' or mymap[y-1][x] in '0123456789':
              this_map[y-1][x] = steps
          if isinstance(mymap[y+1][x], basestring):
            if mymap[y+1][x] == '.' or mymap[y+1][x] in '0123456789':
              this_map[y+1][x] = steps
          if isinstance(mymap[y][x-1], basestring):
            if mymap[y][x-1] == '.' or mymap[y][x-1] in '0123456789':
              this_map[y][x-1] = steps
          if isinstance(mymap[y][x+1], basestring):
            if mymap[y][x+1] == '.' or mymap[y][x+1] in '0123456789':
              this_map[y][x+1] = steps
    mymap = copy.deepcopy(this_map)
    if isinstance(mymap[desty][destx], int):
      return mymap[desty][destx]

for i in range(0, max_num+1):
  for j in range(0, max_num+1):
    distances[i][j] = get_distance(i, j)


all_paths = []
all_nodes = ''
for i in range(1, max_num+1):
  all_nodes+= str(i)


all_paths = ['0'+"".join(perm) for perm in itertools.permutations(all_nodes)]


min_path = 9999999999
this_path_length = 0
for path in all_paths:
  this_path_length = 0
  last_c = ''
  for c in path: 
    if last_c == '':
      last_c = c
      continue
    this_path_length += distances[int(c)][int(last_c)]
    last_c = c
  #print "path: " + path + " -- " + str(this_path_length)
  if this_path_length < min_path:
    min_path = this_path_length


print "Part 1: Shortest path = " + str(min_path)

