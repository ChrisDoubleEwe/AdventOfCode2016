import re
from printf import printf
code =  []

with open("23_b_input.txt") as f:
  for line in f:
    ins = line.strip().split(' ')
    code.append(ins)
reg = {}
reg['a'] = 12
reg['b'] = 0
reg['c'] = 0
reg['d'] = 0
pc = 0




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
    if a == 0:
      return pc+1
    else:
      return pc+int(increment)

def nop():
  return

def mul():
  global reg
  print "MULTIPLY"
  print reg['d']
  print reg['b']


  reg['a'] = reg['d'] * reg['b']
  reg['d'] = 0
  reg['c'] = 0

  print reg
  return 
   
while pc < len(code):
  new_pc = pc+1
  print str(pc) + '  -- ' + str(reg) + " --- " + str(code[pc])
  instruction = code[pc][0]
  if instruction == 'mul':
    mul()
  if instruction == 'nop':
    nop()
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

  pc = new_pc

print reg['a']
