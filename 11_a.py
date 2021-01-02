import re
import copy
from printf import printf

#floors = [['HM', 'LM'], ['HG'], ['LG'], []]
floors = [['TM', 'TG', 'PG', 'SG'], ['PM', 'SM'], ['MG', 'MM', 'RG', 'RM'], []]
seen = []
seen_moves ={}
wins = []

elevator = 0


# Take one thing from current floor in turn
  # Move up one if possible ; drop all
  # Move down one if possible ; drop all

# Take two things from current floor, in all combinations
  # Move up one if possible ; drop all
  # Move down one if possible ; drop all

#End if:
  # Chip is on a floor with any generator, unless is it with its own generator
  # We've seen this state before

#Win if:
  # Everything is on floor 4

def hash(floors, e):
  hash = ':E='+str(e)+":"

  hash += '-1-'
  for a in sorted(floors[0]):
    hash+='+'
    hash+=a
  hash += '-2-'
  for b in sorted(floors[1]):
    hash+='+'
    hash+=b
  hash += '-3-'
  for c in sorted(floors[2]):
    hash+='+'
    hash+=c
  hash += '-4-'
  for d in sorted(floors[3]):
    hash+='+'
    hash+=d
  return hash


def chipFried(f, floors):
  got_chip = 0
  got_generator = 0
  for item in floors[f]:
    if item[1] == 'G':
      got_generator = 1
  for item in floors[f]:
    if item[1] == 'M':
      need = item[0]+'G'
      if got_generator == 1 and need not in floors[f]:
        return True
  return False

def move(result, elevator, a, b, dir, floors):
  global seen
  global seen_moves
  global wins
  # Pick up items
  floors[elevator].remove(a)
  if b!='':
    floors[elevator].remove(b)
  result += 1
  # move elevator
  elevator += dir
  # drop all items
  floors[elevator].append(a)
  if b != '':
    floors[elevator].append(b)
  h = hash(copy.deepcopy(floors), elevator)
  indent_print(result, h)

  if len(floors[0]) + len(floors[1]) + len(floors[2]) == 0:
    indent_print(result, "WON! ALL ITEMS ON FLOOR 4!")
    print result
    wins.append(result)
  for f in range(0, 4):
    if chipFried(f, copy.deepcopy(floors)):
      indent_print(result, "CHIP FRIED!")
      return
  if h in seen:
    if seen_moves[h] <= result:
      indent_print(result, "SEEN THIS")
      return
  seen.append(h)
  seen_moves[h]=result
  
  moves(result, elevator, copy.deepcopy(floors))
  
 
def indent_print(i, s):
  return
  for x in range(0, i):
    printf(' ')
  printf(str(i))
  printf(': ')
  print s 
   
def moves(result, elevator, floors):
  if result > 32:
    return
  indent_print(result, "Moving... ") 
  for item in floors[elevator]:
    if elevator < 3:
      indent_print(result, "Single move up: " + item)
      move(result, elevator, item, '', 1, copy.deepcopy(floors))
    if elevator > 0:
      indent_print(result, "Single move down: " + item)
      move(result, elevator, item, '', -1, copy.deepcopy(floors))
  for i in floors[elevator]:
    for j in floors[elevator]:
      if i == j:
        continue
      if elevator < 3:
        indent_print(result, "Double move up: " + i + " and " + j)
        move(result, elevator, i, j, 1, copy.deepcopy(floors))
      if elevator > 0:
        indent_print(result, "Double move down: " + i + " and " + j)
        move(result, elevator, i, j, -1, copy.deepcopy(floors))

 
moves(0, 0, copy.deepcopy(floors))
min_win = 9999999
for w in wins:
  if w < min_win:
    min_win = w

print "Result: " + str(min_win)
