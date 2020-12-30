pad = []
pad.append(['0','0','0','0','0','0','0'])
pad.append(['0','0','0','1','0','0','0'])
pad.append(['0','0','2','3','4','0','0'])
pad.append(['0','5','6','7','8','9','0'])
pad.append(['0','0','A','B','C','0','0'])
pad.append(['0','0','0','D','0','0','0'])
pad.append(['0','0','0','0','0','0','0'])

x = 1
y = 3

content = []
moves = []
with open("02_input.txt") as f:
  for line in f:
    this_move = []
    print line
    for c in line.strip():
      this_move.append(c)
    moves.append(this_move)

print moves
button = 5

for line in moves:
  for l in line:
    if l == 'R' and pad[x+1][y]!='0':
      x += 1
    if l == 'L' and pad[x-1][y]!='0':
      x -= 1
    if l == 'U' and pad[x][y-1]!='0':
      y -= 1
    if l == 'D' and pad[x][y+1]!='0':
     y += 1
  print pad[y][x]


 

