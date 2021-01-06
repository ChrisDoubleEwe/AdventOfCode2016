import re
from printf import printf
import hashlib

elfs = []
num_elfs = 5
num_elfs = 10

orig_num_elfs = num_elfs

for i in range(0, num_elfs):
  pair = []
  pair.append(i+1)
  pair.append(1)
  elfs.append(pair)


def get_index(x):
  global elfs
  #print "Looking for " + str(x)
  for i in range(0, len(elfs)):
    if elfs[i][0] == x:
      return i

def inc_elf(x):
  global elfs
  while True:
    x = (x+1) % orig_num_elfs
    #print "  looking for elf " + str(x)
    for elf in elfs:
      if elf[0] == x:
        #print "FOUND"
        return x
 
ex = 0
this_elf = 1
while ex == 0:
  print len(elfs)
  this_elf_index = get_index(this_elf)
  offset = int(len(elfs) / 2)
  #print this_elf_index
  #print "offset: " + str(offset)
  opp_elf = (this_elf_index + offset) % num_elfs
  #print "opp elf index: " + str(opp_elf)
  #print elfs[opp_elf]
  elfs[this_elf_index][1] += elfs[opp_elf][1]
  elfs.pop(opp_elf)
  num_elfs += -1
  #print elfs
  if len(elfs) == 1:
    print "DONE"
    print "Final elf: " + str(elfs[0][0])
    exit()
  #print "THIS ELF = " + str(this_elf)
  this_elf = inc_elf(this_elf)
  #print "Next elf: " + str(this_elf)
    
for i in range(0, num_elfs):
  if elfs[i] > 0:
    print "Elf " + str(i+1) + " wins"
    
