import collections

ElvesQ1 = collections.deque()
ElvesQ2 = collections.deque()
for i in range(3012210):
    ElvesQ1.append(i+1)

lenQ1 = 3012210
lenQ2 = 0

while (lenQ1 > lenQ2):
    ElvesQ2.append(ElvesQ1.pop())
    lenQ1 = lenQ1-1
    lenQ2 = lenQ2+1

l = 3012210;
while (l > 1):
    ElvesQ2.pop()
    ElvesQ2.appendleft(ElvesQ1.popleft())
    lenQ1 = lenQ1 - 1
    if ((lenQ2 - lenQ1) > 1):
        ElvesQ1.append(ElvesQ2.pop())
        lenQ1 = lenQ1 + 1
        lenQ2 = lenQ2 - 1
    l = l -1
    

print(ElvesQ1, ElvesQ2)
