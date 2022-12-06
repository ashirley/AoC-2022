import sys, re
stacks = [[], [], [], [], [], [], [], [], []]

setup = True

for line in sys.stdin:
  if setup:
    if len(line) >= 2 and line[1] == '1':
      #this is the end of setup
      setup = False
      for stack in stacks:
        stack.reverse()
      print(stacks)
      continue

    i=0
    while len(line) >= 4 * i + 2:
      c = line[4*i + 1]
      if c != ' ':
        stacks[i].append(c)
      i += 1
  else:
    m = re.search(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)", line)
    if m==None:
      continue
    n = int(m.group(1))
    fromIdx = int(m.group(2))
    toIdx = int(m.group(3))

    for _ in range(n):
      stacks[toIdx-1].append(stacks[fromIdx-1].pop())

print(stacks)
output = ""
for stack in stacks:
  output += stack[-1]

print(output)
