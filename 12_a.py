import re
from printf import printf
code =  []

with open("12_input.txt") as f:
  for line in f:
    ins = line.strip().split(' ')
    code.append(ins)
reg = {}
reg['a'] = 0
reg['b'] = 0
reg['c'] = 1
reg['d'] = 0
pc = 0




def cpy(a, b):
  if a in 'abcd':
    reg[b] = reg[a]
  else:
    reg[b] = int(a)

def inc(a):
  reg[a] += 1

def dec(a):
  reg[a] += -1

def jnz(a, b, pc):
  if a in 'abcd':
    if reg[a] == 0:
      return pc+1
    else:
      return pc+int(b)
  else:
    if a == 0:
      return pc+1
    else:
      return pc+int(b)

   
while pc < len(code):
  new_pc = pc+1
  if code[pc][0] == 'cpy':
    cpy(code[pc][1], code[pc][2]) 
  if code[pc][0] == 'inc':
    inc(code[pc][1])
  if code[pc][0] == 'dec':
    dec(code[pc][1])
  if code[pc][0] == 'jnz':
    new_pc = jnz(code[pc][1], code[pc][2], pc)
  pc = new_pc

print reg['a']
