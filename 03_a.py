triangles = []
valid=0
with open("03_input.txt") as f:
  for line in f:
    side = line.strip().split()
    a = int(side[0])
    b = int(side[1])
    c = int(side[2])
    if a+b>c:
      if a+c>b:
        if b+c>a:
          valid += 1

print valid
