content = []
moves = []
with open("02_test_input.txt") as f:
  for line in f:
    this_move = []
    print line
    for c in line.strip():
      this_move.append(c)
    moves.append(this_move)

print moves
button = 5

for line in moves:
  for x in line:
    if x == 'R' and (button%3)!=0:
      button = button + 1
    if x == 'L' and (button%3)!=1:
      button = button - 1
    if x == 'U' and button>3:
      button = button - 3
    if x == 'D' and button<7:
      button = button + 3
  print button


 

