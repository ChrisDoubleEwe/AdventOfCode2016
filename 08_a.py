import re
from printf import printf

d_width = 50
d_height = 6

display = []
for y in range(0, d_height):
  drow = []
  for x in range(0, d_width):
    drow.append('.')
  display.append(drow)

def print_display():
  print "\n---------------------------------\n"
  for row in display:
    for c in row:
      printf(c)
    print ''

def count_display():
  count = 0
  for row in display:
    for c in row:
      if c == '#':
        count += 1
  print count

print_display()
    

commands = []
with open("08_input.txt") as f:
  for line in f:
    line_split = line.split()
    if line_split[0] == 'rect':
      xy = line_split[1].split('x')
      x = xy[0]
      y = xy[1]
      cmd = []
      cmd.append('rect')
      cmd.append(int(x))
      cmd.append(int(y))
      commands.append(cmd)
    if line_split[0] == 'rotate':
      cmd = []
      cmd.append('rotate')
      cmd.append(line_split[1])
      amt = line_split[2].split('=')
      cmd.append(int(amt[1]))
      cmd.append(int(line_split[4]))
      commands.append(cmd)


for com in commands:
  print com
  if com[0] == 'rect':
    for x in range(0, com[1]):
      for y in range(0, com[2]):
        display[y][x] = '#'
  if com[0] == 'rotate' and com[1] == 'row':
    r = com[2]
    for i in range(0, com[3]):
      row = display[r]
      char = row[-1]
      row = row[:-1]
      display[r] = []
      display[r].append(char)
      display[r].extend(row)
  if com[0] == 'rotate' and com[1] == 'column':
    c = com[2]
    for i in range(com[3]):
      pop_char = display[d_height-1][c]
      for j in range(d_height-1, 0, -1):
        display[j][c] = display[j-1][c]
      display[0][c] = pop_char
              

  print_display()





count_display()
