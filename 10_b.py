import re
from printf import printf

data = []
bots = {}
outputs = {}

max_bot = 0
with open("10_input.txt") as f:
  for line in f:
    match = re.search('value ([0-9]*) goes to bot ([0-9]*)', line)
    if match:
      bot = int(match.group(2))
      val = int(match.group(1))
      if bot in bots.keys():
        pair = []
        existing_val = bots[bot][0]
        pair.append(val)
        pair.append(existing_val)
        bots[bot] = sorted(pair)
      else:
        single = []
        single.append(val)
        bots[bot] = single
      continue
    match = re.search('bot ([0-9]*) gives low to ([a-z]*) ([0-9]*) and high to ([a-z]*) ([0-9]*)', line)
    if match:
      pair = []
      pair.append(int(match.group(1)))
      pair.append(match.group(2))
      pair.append(int(match.group(3)))
      pair.append(match.group(4))
      pair.append(int(match.group(5)))
      data.append(pair)

def give_bot(b, val):
  global bots
  print " -- give " + str(val) + " to bot " + str(b) + " --"
  if b in bots.keys():
    pair = bots[b]
    pair.append(val)
    bots[b] = sorted(pair)
  else:
    single = []
    single.append(val)
    bots[b] = single

def give_output(o, val):
  global outputs
  print " -- give " + str(val) + " to output " + str(o) + " --"
  if o in outputs.keys():
    pair = outputs[o]
    pair.append(val)
    outputs[o] = sorted(pair)
  else:
    single = []
    single.append(val)
    outputs[o] = single


iter = 0
while iter < 10000:
 iter += 1
 for x in data:
  from_bot = x[0]
  if from_bot in bots.keys():
    if len(bots[from_bot]) == 2:
      print "Doing Instruction: "
      print x
      print bots[from_bot]
      low = bots[from_bot][0]
      hi =  bots[from_bot][1]
   
      if hi == 61 and low == 17:
        print "Result: Bot number " + str(from_bot)
      if x[1] == 'bot':
        give_bot(x[2], low)
      else:
        give_output(x[2], low)
      if x[3] == 'bot':
        give_bot(x[4], hi)
      else:
        give_output(x[4], hi)
      bots[from_bot] = []
print "===="
print outputs[0]
print outputs[1]
print outputs[2]

res = int(outputs[0][0]) * int(outputs[1][0]) * int(outputs[2][0])
print res
