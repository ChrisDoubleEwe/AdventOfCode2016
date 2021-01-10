import re
from printf import printf
import copy

code =  []

with open("25_input.txt") as f:
  for line in f:
    ins = line.strip().split(' ')
    code.append(ins)
reg = {}
reg['a'] = 0
reg['b'] = 0
reg['c'] = 0
reg['d'] = 0
pc = 0
output = ''





def tgl(z):
  x = 0
  if z in 'abcd':
    x = reg[z]
  else: 
    x = int(z)
  if pc + x >= len(code):
    return
  if code[pc+x][0] == 'inc':
    code[pc+x][0] = 'dec'
    return
  if code[pc+x][0] == 'dec':
    code[pc+x][0] = 'inc'
    return
  if code[pc+x][0] == 'tgl':
    code[pc+x][0] = 'inc'
    return
  if code[pc+x][0] == 'cpy':
    code[pc+x][0] = 'jnz'
    return
  if code[pc+x][0] == 'jnz':
    code[pc+x][0] = 'cpy'
    return



def cpy(a, b):
  if a in 'abcd':
    reg[b] = reg[a]
    return
  if b in 'abcd':
    reg[b] = int(a)
    return
  return

def inc(a):
  if a in 'abcd':
    reg[a] += 1

def dec(a):
  if a in 'abcd':
    reg[a] += -1

def jnz(a, b, pc):
  increment = 0
  if b in 'abcd':
    increment = reg[b]
  else:
    increment = b
  if a in 'abcd':
    if reg[a] == 0:
      return pc+1
    else:
      return pc+int(increment)
  else:
    if int(a) == 0:
      return pc+1
    else:
      return pc+int(increment)

def out(a):
  global output
  if a in 'abcd':
    output += str(reg[a])
  else:
    output += str(a)


   
output = ''
start = -1
orig_code = copy.deepcopy(code)

while True:
  start += 1
  print "\nTrying " + str(start)
  reg['a'] = start
  reg['b'] = 0
  reg['c'] = 0
  reg['d'] = 0
  pc = 0
  output = ''
  old_pc = -1
  code = copy.deepcopy(orig_code)
  stuck = 0
   
  while pc < len(code) and len(output) < 10 and stuck == 0:
    new_pc = pc+1
    #print str(pc) + '  -- ' + str(code[pc])
    instruction = code[pc][0]
    if instruction == 'out':
      out(code[pc][1])
    if instruction == 'tgl':
      tgl(code[pc][1])
    if instruction == 'cpy':
      cpy(code[pc][1], code[pc][2]) 
    if instruction == 'inc':
      inc(code[pc][1])
    if instruction == 'dec':
      dec(code[pc][1])
    if instruction == 'jnz':
      new_pc = jnz(code[pc][1], code[pc][2], pc)

    if new_pc == pc:
      stuck = 1
    pc = new_pc

  print output
  if output == '0101010101':
     print "GOTCHA! Exiting..."
     exit()

print reg['a']
