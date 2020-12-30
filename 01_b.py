filepath = '01_input.txt'  

a = []
seen = []

with open(filepath) as fp:  
   row = fp.readline()
   while row:
     for x in row.split(','):
       a.append(x.replace(" ", "").rstrip())
     row = fp.readline()


cur_dir = 'N'

def right():
  global cur_dir
  if cur_dir == 'N':
    cur_dir = 'E'
  elif cur_dir == 'E':
    cur_dir = 'S'
  elif cur_dir == 'S':
    cur_dir = 'W'
  elif cur_dir == 'W':
    cur_dir = 'N'

def left():
  global cur_dir
  if cur_dir == 'N':
    cur_dir = 'W'
  elif cur_dir == 'W':
    cur_dir = 'S'
  elif cur_dir == 'S':
    cur_dir = 'E'
  elif cur_dir == 'E':
    cur_dir = 'N'

def check():
  global x
  global y
  global seen
  loc_str = '['+str(x)+','+str(y)+']'
  if loc_str in seen:
    dist = abs(x) + abs(y)
    print dist
    exit()
  else:
    seen.append(loc_str)

x = 0
y = 0
for i in a:
  if i[0] == 'R':
    right()
  if i[0] == 'L':
    left()
  z = int(i[1:])
  if cur_dir == 'N':
    for q in range(0, z):
      y = y + 1
      check()
  if cur_dir == 'S':
    for q in range(0, z):
      y = y - 1
      check()
  if cur_dir == 'E':
    for q in range(0, z):
      x = x + 1
      check()
  if cur_dir == 'W':
    for q in range(0, z):
      x = x - 1
      check()


