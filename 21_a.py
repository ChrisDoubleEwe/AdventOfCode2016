import re
from printf import printf
import copy

ops = []
passwd = 'abcdefgh'
with open("21_input.txt") as f:
  for line in f:
    line_split = line.strip().split(' ')
    ops.append(line_split)

def split(word): 
  return [char for char in word]  

def swap_pos(a, b):
  global passwd
  p_arr = split(passwd)
  print "SWAP POS"
  print a
  print b
  print "BEFORE: " + passwd
  a_char = p_arr[a]
  b_char = p_arr[b]
  p_arr[a] = b_char
  p_arr[b] = a_char
  passwd = ''.join(p_arr)
  print "AFTER:  " + passwd

def swap_letter(a, b):
  global passwd
  print "SWAP LETTER"
  print a
  print b
  print "BEFORE: " + passwd
  passwd = passwd.replace(a, '#')
  passwd = passwd.replace(b, a)
  passwd = passwd.replace('#', b)
  print "AFTER:  " + passwd

def rot_left(a):
  global passwd
  print "ROT L"
  print a
  print "BEFORE: " + passwd
  p_arr = split(passwd)
  for i in range(0, a):
    c = p_arr.pop(0)
    p_arr.append(c)
  passwd = ''.join(p_arr)
  print "AFTER:  " + passwd

def rot_right(a):
  global passwd
  print "ROT R"
  print a
  print "BEFORE: " + passwd
  p_arr = split(passwd)
  for i in range(0, a):
    c = p_arr.pop()
    new_p_arr = []
    new_p_arr.append(c)
    new_p_arr.extend(p_arr)
    p_arr = copy.deepcopy(new_p_arr)
  passwd = ''.join(p_arr)
  print "AFTER:  " + passwd

def rot_based(a):
  global passwd
  print "ROT BASED"
  print a
  print "BEFORE: " + passwd
  pos = passwd.find(a)
  rot_right(1)
  rot_right(pos)
  if pos >= 4:
    rot_right(1)
  print "AFTER:  " + passwd

def rev(a, b):
  global passwd
  print "REV"
  print a
  print b
  print "BEFORE: " + passwd
  pre = passwd[:a]
  mid = passwd[a:b+1]
  post = passwd[b+1:]
  passwd = pre + mid[::-1] + post
  print "AFTER:  " + passwd

def mov(a, b):
  global passwd
  print "MOV"
  print a
  print b
  print "BEFORE: " + passwd
  p_arr = split(passwd)
  c = p_arr.pop(a)
  p_arr.insert(b, c)
  passwd = ''.join(p_arr)
  print "AFTER:  " + passwd

for op in ops:
  print op
  if op[0] == 'swap' and op[1] == 'position':
    swap_pos(int(op[2]), int(op[5]))
  if op[0] == 'swap' and op[1] == 'letter':
    swap_letter(op[2], op[5])
  if op[0] == 'rotate' and op[1] == 'left':
    rot_left(int(op[2]))
  if op[0] == 'rotate' and op[1] == 'right':
    rot_right(int(op[2]))
  if op[0] == 'rotate' and op[1] == 'based':
    rot_based(op[6])
  if op[0] == 'reverse':
    rev(int(op[2]), int(op[4]))
  if op[0] == 'move':
    mov(int(op[2]), int(op[5]))

